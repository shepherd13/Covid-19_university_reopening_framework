# copyright Dakota Olson, Commercial rights reserved.

# -*- coding: utf-8 -*-
import csv
import math
import random
import time
import numpy as np
import pandas as pd
import scipy
import sparse
import os
import copy
from multiprocessing import Pool
from pathlib import Path
from airborne import airborneProb
from airborne import diffProb
from surface_transfer import updatePerson
from export_csv import updateCSV1, updateCSV3
from disease_progression import disease_progression
from MeanSE import getMean
from test_history import run_test
import matplotlib.pyplot as plt


# finds the shape for a weibull distribution, used for hospitalization disease state start and end times
def weibullShape(median, lower, upper):
    ln = -0.366512920581664327012439158232669469454263447837105263053  # ln(ln2)
    return ln / math.log((median - lower) / (upper - lower))


# States: Dead(-2), Recovered (-1), Susceptible (0), Incubating (1), Asymptomatic (2), Symptomatic (3)
# Hospitalized States: Hospitalized (4), Breathing Difficulty (5), Respirator (6), ICU (7)
def run_sim(state, test_state, days_infected, sparse_matrix, class_type, class_sizes, parameters, cur_run, class_length, room_size, infectability, inPerson_people, inPerson_classes):
    #print('Start Run ' + str(cur_run))

    # loads quarantine matrix if necessary
    if (parameters['Quarantine Type'] != 'None'):
        matric = sparse.load_npz(parameters['Quarantine File'])
    else:
        matric = sparse_matrix
    # print(matric)  # test if correct one loaded   

    score = [0] * matric.shape[2]  # score tracking for all locations
    # score_matrix = scipy.sparse.lil_matrix((matric.shape[0], matric.shape[2]))  # keeps track of score each day for each location
    tokens = [parameters['Tokens Per Person']] * matric.shape[1]  # token count for each person

    symptomatic_classes = set([])
    asymptomatic_classes = set([course_id for course_id in range(len(class_type)) if class_type[course_id] == 1])

    # For contact tracing
    class_start_people_infected = []
    class_end_people_infected = []
    people_tested_positive = []

    # *daily* statistics tracking
    susceptible = [0] * (matric.shape[0])
    infected = [0] * (matric.shape[0])
    cumulative_infected = [0] * (matric.shape[0])
    daily_infected = [0] * (matric.shape[0])
    incubating = [0] * (matric.shape[0])
    asymptomatic = [0] * (matric.shape[0])
    symptomatic = [0] * (matric.shape[0])
    recovered = [0] * (matric.shape[0])
    dead = [0] * (matric.shape[0])
    daily_dead = [0] * (matric.shape[0])
    hospitalized = [0] * (matric.shape[0])
    breathing_issue = [0] * (matric.shape[0])
    respirator = [0] * (matric.shape[0])
    icu = [0] * (matric.shape[0])
    people_tested = [] * (matric.shape[0])
    spreader = [0] * (matric.shape[0])
    quarantined = [0] * (matric.shape[0])
    symptomatic_quarantined = [0] * (matric.shape[0])
    symptomatic_tests = [0] * (matric.shape[0])
    contact_trace_tests = [0] * (matric.shape[0])
    extra_tests = [0] * (matric.shape[0])
    positive_symptomatic_tests = [0] * (matric.shape[0])
    positive_contact_trace_tests = [0] * (matric.shape[0])
    positive_extra_tests = [0] * (matric.shape[0])

    # generate age_group of each person
    age_group = ['0-49'] * (matric.shape[1])
    for mnp in range(matric.shape[1]):
        if parameters['Students'] <= mnp:
            age_group[mnp] = random.choices(['0-49','50-64','65+'], [0.25,0.50,0.25])[0]

    # # generate accomodation type dorms/private
    # accomodation = ['p'] * (matric.shape[1])
    # for mnp in range(matric.shape[1]):
    #     if parameters['Students'] > mnp:
    #         accomodation[mnp] = random.choices(['d','p'], [0.20,0.80])[0]

    # generate state start days for each person following weibull, converted to ints
    hosp_start = np.random.weibull(weibullShape(parameters['Hospitalization Median'], parameters['Hospitalization Lower Range'], parameters['Hospitalization Upper Range']), matric.shape[1])
    breath_start = np.random.weibull(weibullShape(parameters['Breath Median'], parameters['Breath Lower Range'], parameters['Breath Upper Range']), matric.shape[1])
    vent_start = np.random.weibull(weibullShape(parameters['Respirator Median'], parameters['Respirator Lower Range'], parameters['Respirator Upper Range']), matric.shape[1])
    icu_start = np.random.weibull(weibullShape(parameters['ICU Median'], parameters['ICU Lower Range'], parameters['ICU Upper Range']), matric.shape[1])
    # hosp_start = [parameters['Hospitalization Median']] * (matric.shape[1])
    # breath_start = [parameters['Breath Median']] * (matric.shape[1])
    # vent_start = [parameters['Respirator Median']] * (matric.shape[1])
    # icu_start = [parameters['ICU Median']] * (matric.shape[1])


    # generate state end dates for each person (saves time then generating a new distribution each time)
    # incub_end = np.random.gamma(2, parameters['Incubation Mean']/2, matric.shape[1])
    # infection_end = np.random.gamma(3, parameters['Infectious Mean']/3, matric.shape[1])
    # hosp_end = np.random.gamma(parameters['Hospitalization Length Mean'], 1, matric.shape[1])
    # icu_end = np.random.gamma(parameters['ICU Length Mean'], 1, matric.shape[1])
    # incub_end = [parameters['Incubation Mean']] * (matric.shape[1])
    incub_end = 1/parameters['Incubation Weibull Lambda'] * np.random.weibull(parameters['Incubation Weibull Alpha'], matric.shape[1])
    infection_end = [parameters['Infectious Mean']] * (matric.shape[1])
    # hosp_end = [parameters['Hospitalization Length Mean']] * (matric.shape[1])
    hosp_end = parameters['Hospitalization Beta Value'] * np.random.weibull(parameters['Hospitalization Alpha Value'], matric.shape[1])
    # icu_end = [parameters['ICU Length Mean']] * (matric.shape[1])
    icu_end = parameters['ICU Beta Value'] * np.random.weibull(parameters['ICU Alpha Value'], matric.shape[1])

    transmission_start = []
    for ie in incub_end:
        transmission_before_days = random.choices([1,2,3], [0.33,0.34,0.33])[0]
        if transmission_before_days < ie:
            transmission_start.append(ie-transmission_before_days)
        else:
            transmission_start.append(ie)
    #transmission_end = np.random.gamma(3.5, parameters['Infectiousness Mean']/3.5, matric.shape[1])
    transmission_end = [parameters['Infectiousness Mean']] * (matric.shape[1])
    infection_start = copy.deepcopy(incub_end)    # Needed another parameter to edit in the disease progeression model in cur_state = 2

    # fix day formats
    for mnp in range(matric.shape[1]):
        hosp_start[mnp] = incub_end[mnp] + parameters['Hospitalization Lower Range'] + (parameters['Hospitalization Upper Range'] - parameters['Hospitalization Lower Range']) * hosp_start[mnp]
        breath_start[mnp] = incub_end[mnp] + parameters['Breath Lower Range'] + (parameters['Breath Upper Range'] - parameters['Breath Lower Range']) * breath_start[mnp]
        vent_start[mnp] = incub_end[mnp] + parameters['Respirator Lower Range'] + (parameters['Respirator Upper Range'] - parameters['Respirator Lower Range']) * vent_start[mnp]
        icu_start[mnp] = incub_end[mnp] + parameters['ICU Lower Range'] + (parameters['ICU Upper Range'] - parameters['ICU Lower Range']) * icu_start[mnp]
        hosp_end[mnp] += hosp_start[mnp]
        icu_end[mnp] += icu_start[mnp]


    ########## Print Statements ############
    #print("incub_end:", np.mean(incub_end))
    #print("transmission_start:", np.mean(transmission_start))
    #print("transmission_end:", np.mean(transmission_end))
    #print("hosp_start:", np.mean(hosp_start))
    #print("hosp_end:", np.mean(hosp_end))
    #print("infection_end:", np.mean(infection_end))
    #print(":", np.mean())


    # iterate through each time-step
    for day_ in range(matric.shape[0]):
        class_start_infected = [[] for i in range(matric.shape[2])]
        class_end_infected = [[] for i in range(matric.shape[2])]
        before_infected = 0
        after_infected = 0
        # # Set classes above certain strength to be online # 1 = offline and # 0 = online
        # class_sizes = matric[day_].sum(axis=0)
        # class_type = list(map(lambda class_size: 1 if class_size < parameters['Upper Limit Offline Class Size'] else 0, class_sizes))

        # offline_classes = list(map(lambda class_size: 1 if class_size < parameters['Upper Limit Offline Class Size'] and class_size > 0 else 0, class_sizes))
        # online_classes = list(map(lambda class_size: 1 if class_size >= parameters['Upper Limit Offline Class Size'] else 0, class_sizes))
        # #print("Day:", day_)
        # #print("Total Online classes:", sum(online_classes))
        # #print("Total Offline classes:", sum(offline_classes))
        # offline_students = 0
        # online_students = 0


        check_ins = matric[day_, :, :].nonzero()

        # counts total quanta in room
        total_quanta = [0] * (matric.shape[2])

        for visit_ in range(len(check_ins[0])):
            pers_, course_ = (check_ins[0][visit_], check_ins[1][visit_])

            if day_ < 14:
                continue

            if class_type[course_] == 0:
                continue

            # if asymptomatic spreader (assuming symptomatic people stay home)
            if state[day_, pers_] == 2 or state[day_, pers_] == 9:
                class_start_infected[course_].append(pers_)
                before_infected += 1
                # this is if using two matrices, accepts two different mask rates + efficiencies (types)
                if parameters['Students'] > pers_:
                    ratio = 1.0 - (parameters['Mask Rate'] * parameters['Mask Efficiency'])
                    total_quanta[course_] += parameters['Quant Rate'] * ratio
                else:
                    ratio2 = 1.0 - (parameters['Mask Rate 2'] * parameters['Mask Efficiency 2'])
                    total_quanta[course_] += parameters['Quant Rate'] * ratio2

        #print("Total Quanta", sum(total_quanta))
        #print("Total Offline Students:", offline_students)

        # processes visits (classes)
        for visit in range(len(check_ins[0])):
            pers, course = (check_ins[0][visit], check_ins[1][visit])

            if day_ < 14:
                continue

            #online or offline || 0 or 1
            if class_type[course] == 0:
                continue

            # if susceptible and room quanta not 0 (saves computations)
            if state[day_, pers] == 0 and total_quanta[course] != 0:
                room_volume = 5 + (room_size[course] * ((parameters['Density'] * 12) / 35.315))  # sq ft to sq meter

                # if person is a student
                if parameters['Students'] > pers:
                    # randomly determines if susceptible person is wearing a mask
                    wearing_mask = random.choices([False, True], [1.0 - parameters['Mask Rate'], parameters['Mask Rate']])[0]

                    # diffprob is the differentiated wells-riley, airborneprob is the normal, airSpread is the prob of infection for the person
                    # IN FUTURE WE WILL It will get
                    airSpread = diffProb(class_length[course], total_quanta[course], wearing_mask, room_volume, parameters['Vent Rate'], parameters['Mask Efficiency'])
                    if (random.choices([0, 1], [1.0 - airSpread, airSpread])[0] == 1):
                        state[day_, pers] = 1   # infected, incubating
                        class_end_infected[course].append(pers)
                        after_infected += 1
                        if parameters['Professor Mode'] != 1:
                            daily_infected[day_] += 1

                # if person is an instructor
                else:
                    # randomly determines if susceptible person is wearing a mask
                    wearing_mask = random.choices([False, True], [1.0 - parameters['Mask Rate 2'], parameters['Mask Rate 2']])[0]

                    airSpread = diffProb(class_length[course], total_quanta[course], wearing_mask, room_volume, parameters['Vent Rate'], parameters['Mask Efficiency 2'])
                    if (random.choices([0, 1], [1.0 - airSpread, airSpread])[0] == 1):
                        state[day_, pers] = 1   # infected, incubating
                        class_end_infected[course].append(pers)
                        daily_infected[day_] += 1
                        after_infected += 1


        # reset tokens
        if ((day_ - parameters['Token Policy Start']) % parameters['Token Policy Length'] == 0):
            tokens = [parameters['Tokens Per Person']] * matric.shape[1]
            # print("Tokens Resets Day: " + str(day_))

        # surface transfer code

        # iterates through all check_ins on current step
        # for p_ind in range(len(check_ins[0])):
        #    # surface transfer model
        #    if (day_ < parameters['Token Policy Start'] or tokens[check_ins[0][p_ind]] != 0):
        #        # no policy in effect
        #        if(day_ < parameters['Policy 1 Start']):
        #            daily_infected[day_] += updatePerson(day_, check_ins[0][p_ind], check_ins[1][p_ind], score, state, parameters)
        #            tokens[check_ins[0][p_ind]] -= 1  # reduce token count
        #        
        #        # policy 1 in effect
        #        elif(day_ < parameters['Policy 2 Start']):
        #            if (random.choices([0, 1], [parameters['Stay Home Compliance 1'] * parameters['Location Max Capacity 1'], 1.0 - (parameters['Stay Home Compliance 1'] * parameters['Location Max Capacity 1'])])[0] == 1):
        #                daily_infected[day_] += updatePerson(day_, check_ins[0][p_ind], check_ins[1][p_ind], score, state, parameters)
        #                tokens[check_ins[0][p_ind]] -= 1
        #        
        #        elif (random.choices([0, 1], [parameters['Stay Home Compliance 2'] * parameters['Location Max Capacity 2'], 1.0 - (parameters['Stay Home Compliance 2'] * parameters['Location Max Capacity 2'])])[0] == 1):
        #            daily_infected[day_] += updatePerson(day_, check_ins[0][p_ind], check_ins[1][p_ind], score, state, parameters)
        #            tokens[check_ins[0][p_ind]] -= 1     
        #
        #        else:
        #            print('Policy 2 Blocked Visit')
        #    else:
        #        print('Token Blocked, Day: ' + str(day_))
        
        # decays location score
        for cur_loc in range(matric.shape[2]):
            score[cur_loc] = score[cur_loc] * math.exp(-24 / parameters['Mean Decay Length'])  # exponential decay
            # score_matrix[day_, cur_loc] = score[cur_loc]  # for ouputting daily scores

        symptomatic_classes_left, symptomatic_classes_removed, st, ctt, et, pst, pctt, pet = run_test(matric, day_, state, test_state, parameters, infectability,
                                                                inPerson_people, inPerson_classes, symptomatic_classes, asymptomatic_classes)
        symptomatic_tests[day_] = st
        contact_trace_tests[day_] = ctt
        extra_tests[day_] = et
        positive_symptomatic_tests[day_] = pst
        positive_contact_trace_tests[day_] = pctt
        positive_extra_tests[day_] = pet

        # run disease progression model
        disease_progression(matric, day_, state, test_state, days_infected, incub_end, parameters, infection_start, infection_end, hosp_start, 
            breath_start, hosp_end, vent_start, icu_start, icu_end, age_group, transmission_start, transmission_end)

        # collect stats
        for person in range(matric.shape[1]):
            if (parameters['Professor Mode'] != 1 and parameters['Students'] > person) or (parameters['Professor Mode'] == 1 and parameters['Students'] <= person):
                cur_state = state[day_, person]
                if(cur_state == 0):
                    susceptible[day_] += 1

                elif(cur_state == 1):
                    incubating[day_] += 1
                    infected[day_] += 1          

                elif(cur_state == 2):
                    asymptomatic[day_] += 1 
                    infected[day_] += 1

                elif(cur_state == 3):
                    symptomatic[day_] += 1 
                    infected[day_] += 1

                elif(cur_state == -1):
                    recovered[day_] += 1 

                elif(cur_state == -2):
                    dead[day_] += 1
                    
                elif(cur_state == 7):
                    icu[day_] += 1
                    respirator[day_] += 1
                    breathing_issue[day_] += 1
                    hospitalized[day_] += 1
                    infected[day_] += 1

                elif(cur_state == 6):
                    respirator[day_] += 1
                    breathing_issue[day_] += 1
                    hospitalized[day_] += 1
                    infected[day_] += 1

                elif(cur_state == 5):
                    breathing_issue[day_] += 1
                    hospitalized[day_] += 1
                    infected[day_] += 1

                elif(cur_state == 4):
                    hospitalized[day_] += 1
                    infected[day_] += 1

                elif(cur_state == 8):
                    infected[day_] += 1

                elif(cur_state == 9):
                    infected[day_] += 1
                    asymptomatic[day_] += 1

                elif(cur_state == 10):
                    infected[day_] += 1
                    symptomatic_quarantined[day_] += 1

            # set states for next day
            if (day_ + 1) != matric.shape[0]:
                state[day_ + 1, person] = state[day_, person]

            # if day_ > 0:
            #     if state[day_ - 1 , person] == 0 and state[day_, person] == 1:
            #         accomodation_type = accomodation[person]
            #         total_offline_classes = enrollment_record
            #         for course_id in list(enrollment_record.loc[enrollment_record['student_id'] == person, 'course_id'])

        # With "Outside Transmission Rate" probability one susceptible non-quarantined person will get infected each day
        otr = copy.deepcopy(parameters['Outside Transmission Rate'])
        while otr > 0.0 and (day_ + 1) != matric.shape[0]:
            if otr < 1:
                while True: 
                    person_ = random.choice(range(matric.shape[1]))
                    if state[day_, person_] == 0:
                        state[day_ + 1, person_] = random.choices([0, 1], [1.0 - parameters['Outside Transmission Rate'], parameters['Outside Transmission Rate']])[0]
                        if state[day_ + 1, person_] == 1:
                            daily_infected[day_] += 1
                            infected[day_] += 1
                            incubating[day_] += 1
                        break
            else:
                while True: 
                    person_ = random.choice(range(matric.shape[1]))
                    if state[day_, person_] == 0:
                        state[day_ + 1, person_] = 1
                        daily_infected[day_] += 1
                        infected[day_] += 1
                        incubating[day_] += 1
                        break
            otr -= 1.0

        # more stats
        #spreader[day_] = spreader[day_] + asymptomatic[day_]
        spreader[day_] =  len(set([person_ for class_ in class_start_infected for person_ in class_]))
        #quarantined[day_] = infected[day_] - spreader[day_]
        quarantined[day_] = symptomatic_quarantined[day_]

        if day_ == 0:
            cumulative_infected[day_] = infected[day_]# + incubating[day_]
            daily_dead[day_] = dead[day_]

        else:
            cumulative_infected[day_] = cumulative_infected[day_ - 1] + daily_infected[day_]
            daily_dead[day_] = dead[day_] - dead[day_ - 1]
        

        symptomatic_classes = symptomatic_classes_left
        people_tested.append(len(test_state[day_,:].nonzero()[1]))
        people_tested_positive = (test_state[day_,:]==1).nonzero()[1]
        for person_ in people_tested_positive:
            enrolled_courses = [course_id for day in range(5) for course_id in matric[day,person_].nonzero()[0]]
            for course_id in enrolled_courses:
                if class_type[course_id] == 1:
                    symptomatic_classes.add(course_id)
                    try:
                        asymptomatic_classes.remove(course_id)
                    except:
                        pass

        for course_id in symptomatic_classes_removed:
            asymptomatic_classes.add(course_id)

        #print("Day:", day_, "Positive cases:", len(people_tested_positive), "Symptomatic classes:", len(symptomatic_classes), "Asymptomatic classes:", len(asymptomatic_classes))
        #print(people_tested)

        # Testing details
        """
        print("Day:", day_)
        total_inPerson_people = []
        for day in range(5):
            total_inPerson_people = list(set(total_inPerson_people) | set(inPerson_people[day]))
        print("In person People",len(total_inPerson_people))

        people_last_tested = [0] * len(total_inPerson_people)
        if day >= parameters['Testing Days Gap']:
            for person_ in range(len(total_inPerson_people)):
                people_last_tested[person_] = sum(test_state[day-int(parameters['Testing Days Gap']):day, total_inPerson_people[person_]])
        else:
            for person_ in range(len(total_inPerson_people)):
                people_last_tested[person_] = sum(test_state[0:day, total_inPerson_people[person_]])

        tested_people = 0
        for p in range(len(total_inPerson_people)):
            if people_last_tested[p] != 0:
                tested_people += 1
        print("People Tested",tested_people)
        print("People Left",len(total_inPerson_people) - tested_people)
        """
        #print("Day:", day_, "Infected Before:", before_infected, "Infected After:", after_infected)
        class_start_people_infected.append(class_start_infected)
        class_end_people_infected.append(class_end_infected)

    # export current infected
    #export_file = parameters['Output Directory'] + str(cur_run) + '_current_start_infected.csv'
    #updateCSV3(export_file, class_start_people_infected)

    #export_file = parameters['Output Directory'] + str(cur_run) + '_current_end_infected.csv'
    #updateCSV3(export_file, class_end_people_infected)
    # exports results
    export_file = parameters['Output Directory'] + str(cur_run) + '.csv'
    updateCSV1(export_file, susceptible, infected, cumulative_infected, daily_infected, incubating, asymptomatic, 
        symptomatic, recovered, dead, daily_dead, hospitalized, breathing_issue, respirator, icu, parameters, people_tested,
        spreader, quarantined, symptomatic_tests, contact_trace_tests, extra_tests, positive_symptomatic_tests, positive_contact_trace_tests, positive_extra_tests)


def main(param_file, runs):
    base_path = Path(__file__).parent  # absolute working directory path

    # Read parameters from file
    params = open(base_path / param_file, 'r')
    parameters = {}  # empty parameter dictionary
    for x in params:
        x = x.rstrip()
        x = x.split(': ')
        try:
            float(x[1])
            parameters[x[0]] = float(x[1])  # creates dictionary with parameters
        except ValueError:
            parameters[x[0]] = x[1]  # creates dictionary with parameters
    params.close()

    sparse_matrix = sparse.load_npz(base_path / parameters['Network'])
    #print(sparse_matrix)  # prints network info (for testing)
    
    temp = parameters['Output Directory']
    output = base_path / parameters['Output Directory']

    # remove dirctory if empty
    try:
        os.rmdir(output)
    except OSError as ex:
        pass
    
    os.mkdir(output)

    # set parameters
    parameters['Output Directory'] = str(output) + '/'
    parameters['Students'] = sparse_matrix.shape[1]  # only used with two networks
    parameters['Adjusted ICU'] = parameters['ICU Rate'] / parameters['Breath Rate']  # adjusts ICU rate for simulation
    parameters['Adjusted ICU 2'] = parameters['ICU Rate 2'] / parameters['Breath Rate 2']  # adjusts ICU rate for simulation


    # get course length and room sizes from csv
    if parameters['Class Mode'] == 1:
        class_file = str(base_path / parameters['Courses'])
        df = pd.read_csv(class_file, usecols = ['start','end', 'capacity'])
        df['start'] = pd.to_datetime(df['start'])
        df['end'] = pd.to_datetime(df['end'])

        # calculate difference between start and end times in hours
        df['diff'] = df['end'] - df['start']
        df['diff'] = df['diff'] / np.timedelta64(1,'h')

        # get capacity and class start and end times from course_info csv
        class_length = df['diff'].tolist()
        room_size = df['capacity'].tolist()

    # adds the two networks together, results ONLY report for second network
    if parameters['Other Network'] != 'None':
        temp_matrix = sparse.load_npz(base_path / parameters['Other Network'])
        sparse_matrix = sparse.concatenate((sparse_matrix, temp_matrix), axis=1)
        # print(sparse_matrix)  # prints network info (for testing)

    # In person and Online class distribution
    classes_type = [0] * (sparse_matrix.shape[2])
    classes_size = [0] * (sparse_matrix.shape[2])
    inPerson_classes = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
    inPerson_people = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
    # inPerson_infectability = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
    for day in range(5):
        sizes = sparse_matrix[day].sum(axis=0)
        for class_id in range(sparse_matrix.shape[2]):
            classes_size[class_id] = max(classes_size[class_id], sizes[class_id])

    for class_id in range(sparse_matrix.shape[2]):
        if classes_size[class_id] <= parameters['Upper Limit Offline Class Size'] and classes_size[class_id] > 1:
            classes_type[class_id] = 1

    for day in range(5):
        sizes = sparse_matrix[day].sum(axis=0)
        for course in range(sparse_matrix.shape[2]):
            if (sizes[course] <= parameters['Upper Limit Offline Class Size'] and sizes[course] > 1):
                inPerson_classes[day].append(course)
                inPerson_people[day] = list(set(inPerson_people[day]) | set(sparse_matrix[day,:,course].nonzero()[0]))


    # calculate infectability
    infectability = [0] * (sparse_matrix.shape[1])
    for person in range(sparse_matrix.shape[1]):
        enrolled_courses = [course_id for day in range(5) for course_id in sparse_matrix[day,person].nonzero()[0]]
        infection = sum([classes_size[course_id] for course_id in enrolled_courses if classes_type[course_id] == 1])
        if infection == 0:
            infectability[person] = 0
        else: 
            infectability[person] = math.log(infection, 2) # infectability = log(weekly interactions, 2)
        # print("person:", person)
        # print("courses:", enrolled_courses)
        # print ("Infectability:", infectability[person])
    # ds = [infection for infection in infectability if infection > 0]
    # num_bins = 100
    # a = plt.hist(ds, num_bins, facecolor='blue', alpha=0.5)

    # with open('person_infectability.csv', 'w+', newline = '') as f:
    #     writer = csv.writer(f)
    #     l = []
    #     writer.writerow(l)

    #     l.append('NumPerson')
    #     l.append('Infectability')
    #     writer.writerow(l)
    #     for i in range(len(a[0])):
    #         l = []
    #         l.append(a[0][i])
    #         l.append(a[1][i])
    #         writer.writerow(l)
    # f.close()
    #n, bins, patches = plt.hist(ds, num_bins, facecolor='blue', alpha=0.5)
    #plt.show()

    for day in range(5):
        print("Day:", day, "In person Classes",len(inPerson_classes[day]), "In person People",len(inPerson_people[day]))

    # for day in range(5):
    #     course_people_infectability = {person_:infectability[person_] for person_ in inPerson_people[day]}
    #     inPerson_infectability[day] = [(k,v) for k, v in sorted(course_people_infectability.items(), key=lambda item: item[1])][::-1]

    # set more parameters
    parameters['Threshold'] = 0.0034 * sparse_matrix.shape[1]  # used for calculating likelihood of catching disease, scaled with population size
    parameters['Patient Zero'] = sparse_matrix.shape[1] * parameters['Initial Infected Population']
    # if parameters['Test Upon Entry']:
    #     Initially_infected = sparse_matrix.shape[1] * parameters['Initial Infected Population']
    #     False_positve_cases = (sparse_matrix.shape[1] - Initially_infected) * parameters['Asymptomatic False Positive Rate']
    #     False_negative_cases = Initially_infected * parameters['Asymptomatic False Negative Rate']
    #     parameters['Patient Zero'] =  Initially_infected - False_negative_cases + False_positve_cases # number of seeded infected, scaled with population size
    # else:
    #     parameters['Patient Zero'] = sparse_matrix.shape[1] * parameters['Initial Infected Population']
    print("Seeds:", parameters['Patient Zero'])
    
    p = Pool(processes=1)  # max 10 processes

    for i in range(runs):
        # iteration seeding start
        seed = scipy.sparse.lil_matrix((sparse_matrix.shape[0], sparse_matrix.shape[1]))  # modifiable time person matrix
        test_state = scipy.sparse.lil_matrix((sparse_matrix.shape[0], sparse_matrix.shape[1]))
        #test_state[0,:] = 0
        days_infected = [0] * sparse_matrix.shape[1]  # days infected for each person

        uniqueDay0 = np.unique(sparse_matrix[0, :, :].nonzero())  # gets unique users from first day
        z = 0  # tracks number seeded (to prevent seeding same person twice)

        while z < parameters['Patient Zero']:  # sets n number of check-ins on day 0 to infection
            pat_zero = random.choice(uniqueDay0)  # get random person
            if (z == 0):  # guaranatees a spreader
                seed[0, pat_zero] = 2  # asymptomatic spreader
                days_infected[pat_zero] = int(parameters['Incubation Mean'])
                #days_infected[pat_zero] = int(parameters['Incubation Mean']) - 2
                z += 1

            elif (seed[0, pat_zero] == 0):
                seed[0, pat_zero] = 1  # start as incubating
                days_infected[pat_zero] = int((parameters['Incubation Mean'] - 1) - (z % (parameters['Incubation Mean'] - 1)))
                #days_infected[pat_zero] = int((parameters['Incubation Mean'] - 3) - (z % (parameters['Incubation Mean'] - 3)))
                z += 1

        #extra_test_capacity = parameters['Test Capacity']
        #run_test(sparse_matrix, 0, seed, test_state, parameters, extra_test_capacity, infectability, inPerson_people, inPerson_classes, test_classes)

        #run_sim(seed, test_state, days_infected, sparse_matrix, classes_type, classes_size, parameters, i, class_length, room_size, infectability, inPerson_people, inPerson_classes)

        p.apply_async(run_sim, args=(seed, test_state, days_infected, sparse_matrix, classes_type, classes_size, parameters, i, class_length, room_size, infectability, inPerson_people, inPerson_classes, ))
        # scipy.sparse.save_npz(first_save_loc + '/state_matrix.npz', seed.tocoo())
    p.close()
    p.join()
    # find mean, standard error and auto generates an SEIR graph
    getMean( sparse_matrix.shape[0], parameters['Output Directory'], temp)

if __name__ == "__main__":
#def run():
    np.seterr(all='raise')
    number_of_runs = 2  # they run in parallel
    start_time = time.time()
    
    main('template.txt', number_of_runs)

    print("Run Time (seconds): " + str(time.time() - start_time))
    print('Sims Done')
