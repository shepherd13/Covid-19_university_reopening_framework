 # -*- coding: utf-8 -*-
import math
import random

# States: Dead(-2), Recovered (-1), Susceptible (0), Incubating (1), Asymptomatic (2), Symptomatic (3), Asymptomatic Quarantined (8), Symptomatic Spreader (9),Symptomatic Quarantined (10)
# Hospitalized States: Hospitalized (4), Breathing Difficulty (5), Respirator (6), ICU (7)

def disease_progression(matric, day, state, test_state, days_infected, incub_end, parameters, infection_start, infection_end, hosp_start, breath_start, hosp_end, vent_start, icu_start, icu_end, age_group, transmission_start, transmission_end):
    for person in range(matric.shape[1]):
        cur_state = state[day, person]
        cur_test_state = test_state[day, person]

        # if some form of infected
        if cur_state > 0 and parameters['Students'] > person:
            days_infected[person] += 1  # increases number of days person has been infected

            # incubating
            if cur_state == 1:
                if cur_test_state == 1: # If test turns out positive
                    state[day, person] = 8  # Quarantined
                else:
                    # tests if incubation is done
                    if days_infected[person] >= transmission_start[person]:
                        state[day, person] = 2  # transmitting

                    if transmission_start[person] == incub_end[person]:
                        # roll if asymptomatic or symptomatic
                        if (random.choices([0, 1], [parameters['Asymptomatic Rate'], 1.0 - parameters['Asymptomatic Rate']])[0] == 1):
                            state[day, person] = 3  # symptomatic
            
            # asymptomatic
            elif cur_state == 2:
                if cur_test_state == 1: # If test turns out positive
                    state[day, person] = 8  # Quarantined
                else:
                    #if days_infected[person] >= incub_end[person]:
                    if days_infected[person] >= infection_start[person]:
                        infection_start[person] = 1000
                        if (random.choices([0, 1], [parameters['Asymptomatic Rate'], 1.0 - parameters['Asymptomatic Rate']])[0] == 1):
                            state[day, person] = 3  # symptomatic
                    # if infection over
                    if (days_infected[person] - transmission_start[person]) >= transmission_end[person]:
                        state[day, person] = -1  # recovered
                        #print("Asymptomatic Recovered:", "Day=", day, "Person=", person, "Days infected", days_infected[person], "Transmission Start", transmission_start[person], "Transmission End", transmission_end[person])

            # symptomatic
            elif cur_state == 3:
                if cur_test_state == -1: # If test turns out negative
                    state[day, person] = 9  # symptomatic spreader
                elif cur_test_state == 1:
                    state[day, person] = 10  # symptomatic quarantined
                #else:
                    #state[day,person] = 9

            # hospitalized
            elif cur_state == 4:
                if (days_infected[person] - incub_end[person]) >= breath_start[person]:
                    breath_start[person] = 1000  # prevents rolling twice
                    # roll if shortness of breath
                    if (random.choices([0, 1], [1.0 - parameters['Breath Rate'], parameters['Breath Rate']])[0] == 1):
                        state[day, person] = 5  # shortness of breath

                elif (days_infected[person] - incub_end[person]) >= hosp_end[person]:
                    if random.choices([0, 1], [1.0 - parameters['Hospitalization Death Rate 0-49'], parameters['Hospitalization Death Rate 0-49']])[0] == 1:
                        state[day, person] = -2  # dead
                    # recovered
                    else:
                        state[day, person] = -1  # recovered
                        #print("Hospitalized Recovered:", "Day=", day, "Person=", person)

            # breathing issue
            elif cur_state == 5:
                if (days_infected[person] - incub_end[person]) >= vent_start[person]:
                    vent_start[person] = 1000  # prevents rolling twice
                    # roll if respirator
                    if (random.choices([0, 1], [1.0 - parameters['Respirator Rate'], parameters['Respirator Rate']])[0] == 1):
                        state[day, person] = 6  # respirator

                elif (days_infected[person] - incub_end[person]) >= icu_start[person]:
                    icu_start[person] = 1000  # prevents rolling twice
                    # roll if icu
                    if (random.choices([0, 1], [1.0 - parameters['Adjusted ICU'], parameters['Adjusted ICU']])[0] == 1):
                        state[day, person] = 7  # icu

                elif (days_infected[person] - incub_end[person]) >= hosp_end[person]:
                    if random.choices([0, 1], [1.0 - parameters['Breath Death Rate'], parameters['Breath Death Rate']])[0] == 1:
                        state[day, person] = -2  # dead
                    # recovered
                    else:
                        state[day, person] = -1  # recovered

            # Respirator
            elif cur_state == 6:
                if (days_infected[person] - incub_end[person]) >= icu_start[person]:
                    icu_start[person] = 1000  # can't roll twice
                    # roll if icu
                    if (random.choices([0, 1], [1.0 - parameters['Adjusted ICU'], parameters['Adjusted ICU']])[0] == 1):
                        state[day, person] = 7  # icu

                elif (days_infected[person] - incub_end[person]) >= hosp_end[person]:
                    if random.choices([0, 1], [1.0 - parameters['Respirator Death Rate'], parameters['Respirator Death Rate']])[0] == 1:
                        state[day, person] = -2  # dead
                    # recovered
                    else:
                        state[day, person] = -1  # recovered

            # ICU       
            elif cur_state == 7:
                if (days_infected[person] - incub_end[person]) >= icu_end[person]:
                    if random.choices([0, 1], [1.0 - parameters['ICU Death Rate'], parameters['ICU Death Rate']])[0] == 1:
                        state[day, person] = -2  # dead
                    # recovered
                    else:
                        state[day, person] = -1  # recovered

            # Quarantined
            elif cur_state == 8:
                if len(test_state[:, person].nonzero()[1]) >= 1:
                    days_since_tested = day - test_state[:, person].nonzero()[1][-1]
                    if (days_since_tested - incub_end[person]) >= infection_end[person]:
                        state[day, person] = -1  # recovered

            # Symptomatic Spreader
            elif cur_state == 9:
                if cur_test_state == 1: # If test turns out positive
                    state[day, person] = 10  # Symptomatic
                else:
                    if len(test_state[:, person].nonzero()[1]) >= 1:
                        days_since_tested = day - test_state[:, person].nonzero()[1][-1]
                        if(days_since_tested - incub_end[person]) >= infection_end[person]:
                            state[day, person] = -1  # recovered
                            #print("Symptomatic Spreader Recovered:", "Day=", day, "Person=", person)

            elif cur_state == 10:
                if days_infected[person] >= hosp_start[person]:
                    hosp_start[person] = 1000  # prevents rolling twice
                    # roll if hospitalized
                    if (random.choices([0, 1], [1.0 - parameters['Hospitalization Rate 0-49'], parameters['Hospitalization Rate 0-49']])[0] == 1):
                        state[day, person] = 4  # hospitalized

                # if infection over
                elif (days_infected[person] - incub_end[person]) >= infection_end[person]:
                    # death roll for non-hospitalized
                    if random.choices([0, 1], [1.0 - parameters['Infectious Death Rate'], parameters['Infectious Death Rate']])[0] == 1:
                        state[day, person] = -2  # dead
                    # recovered
                    else:
                        state[day, person] = -1  # recovered
                        #print("Symptomatic Quarrantines Recovered:", "Day=", day, "Person=", person)


        # uses the other hospitalization / icu / etc rates for the 2nd network
        elif cur_state > 0 and parameters['Students'] <= person:
            days_infected[person] += 1  # increases number of days person has been infected

            # incubating
            if cur_state == 1:
                if cur_test_state == 1: # If test turns out positive
                    state[day, person] = 8  # Quarantined
                else:
                    # tests if incubation is done
                    if days_infected[person] >= transmission_start[person]:
                        state[day, person] = 2  # transmitting

                    if transmission_start[person] == incub_end[person]:
                        # roll if asymptomatic or symptomatic
                        if (random.choices([0, 1], [parameters['Asymptomatic Rate'], 1.0 - parameters['Asymptomatic Rate']])[0] == 1):
                            state[day, person] = 3  # symptomatic
            
            # asymptomatic
            elif cur_state == 2:
                if cur_test_state == 1: # If test turns out positive
                    state[day, person] = 8  # Quarantined
                else:
                    if days_infected[person] >= incub_end[person]:
                        if (random.choices([0, 1], [parameters['Asymptomatic Rate'], 1.0 - parameters['Asymptomatic Rate']])[0] == 1):
                            state[day, person] = 3  # symptomatic
                    # if infection over
                    if (days_infected[person] - transmission_start[person]) >= transmission_end[person]:
                        state[day, person] = -1  # recovered

            # symptomatic
            elif cur_state == 3:
                if cur_test_state == -1: # If test turns out negative
                    state[day, person] = 9  # symptomatic spreader
                elif cur_test_state == 1:
                    state[day, person] = 10  # symptomatic quarantined

            # hospitalized
            elif cur_state == 4:
                if (days_infected[person] - incub_end[person]) >= breath_start[person]:
                    breath_start[person] = 1000  # can't roll twice
                    # roll if shortness of breath
                    if (random.choices([0, 1], [1.0 - parameters['Breath Rate 2'], parameters['Breath Rate 2']])[0] == 1):
                        state[day, person] = 5  # shortness of breath

                elif (days_infected[person] - incub_end[person]) >= hosp_end[person]:
                    #print("Type of something : ", type(parameters['Hospitalization Death Rate ' + age_group[person]]), age_group[person])
                    if random.choices([0, 1], [1.0 - parameters['Hospitalization Death Rate ' + age_group[person]], parameters['Hospitalization Death Rate ' + age_group[person]]])[0] == 1:
                        state[day, person] = -2
                    # recovered
                    else:
                        state[day, person] = -1

            # breathing issue
            elif cur_state == 5:
                if (days_infected[person] - incub_end[person]) >= vent_start[person]:
                    vent_start[person] = 1000  # can't roll twice
                    # roll if respirator
                    if (random.choices([0, 1], [1.0 - parameters['Respirator Rate 2'], parameters['Respirator Rate 2']])[0] == 1):
                        state[day, person] = 6  # respirator

                elif (days_infected[person] - incub_end[person]) >= icu_start[person]:
                    icu_start[person] = 1000  # can't roll twice
                    # roll if icu
                    if (random.choices([0, 1], [1.0 - parameters['Adjusted ICU 2'], parameters['Adjusted ICU 2']])[0] == 1):
                        state[day, person] = 7  # icu

                elif (days_infected[person] - incub_end[person]) >= hosp_end[person]:
                    if random.choices([0, 1], [1.0 - parameters['Breath Death Rate 2'], parameters['Breath Death Rate 2']])[0] == 1:
                        state[day, person] = -2
                    # recovered
                    else:
                        state[day, person] = -1

            # Respirator
            elif cur_state == 6:
                if (days_infected[person] - incub_end[person]) >= icu_start[person]:
                    icu_start[person] = 1000  # can't roll twice
                    # roll if icu
                    if (random.choices([0, 1], [1.0 - parameters['Adjusted ICU 2'], parameters['Adjusted ICU 2']])[0] == 1):
                        state[day, person] = 7  # icu

                elif (days_infected[person] - incub_end[person]) >= hosp_end[person]:
                    if random.choices([0, 1], [1.0 - parameters['Respirator Death Rate 2'], parameters['Respirator Death Rate 2']])[0] == 1:
                        state[day, person] = -2
                    # recovered
                    else:
                        state[day, person] = -1

            # ICU       
            elif cur_state == 7:
                if (days_infected[person] - incub_end[person]) >= icu_end[person]:
                    if random.choices([0, 1], [1.0 - parameters['ICU Death Rate 2'], parameters['ICU Death Rate 2']])[0] == 1:
                        state[day, person] = -2
                    # recovered
                    else:
                        state[day, person] = -1

            # Quarantined
            elif cur_state == 8:
                if len(test_state[:, person].nonzero()[1]) >= 1:
                    days_since_tested = day - test_state[:, person].nonzero()[1][-1]
                    if (days_since_tested - incub_end[person]) >= infection_end[person]:
                        state[day, person] = -1  # recovered

            # Symptomatic Spreader
            elif cur_state == 9:
                if cur_test_state == 1: # If test turns out positive
                    state[day, person] = 10  # Symptomatic
                else:
                    if len(test_state[:, person].nonzero()[1]) >= 1:
                        days_since_tested = day - test_state[:, person].nonzero()[1][-1]
                        if(days_since_tested - incub_end[person]) >= infection_end[person]:
                            state[day, person] = -1  # recovered

            elif cur_state == 10:
                if days_infected[person] >= hosp_start[person]:
                    hosp_start[person] = 1000  # prevents rolling twice
                    # roll if hospitalized
                    if (random.choices([0, 1], [1.0 - parameters['Hospitalization Rate ' + age_group[person]], parameters['Hospitalization Rate ' + age_group[person]]])[0] == 1):
                        state[day, person] = 4  # hospitalized

                # if infection over
                elif (days_infected[person] - incub_end[person]) >= infection_end[person]:
                    # death roll for non-hospitalized
                    if random.choices([0, 1], [1.0 - parameters['Infectious Death Rate 2'], parameters['Infectious Death Rate 2']])[0] == 1:
                        state[day, person] = -2
                    # recovered
                    else:
                        state[day, person] = -1
