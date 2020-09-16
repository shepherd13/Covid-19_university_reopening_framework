 # -*- coding: utf-8 -*-
import csv

def updateCSV1(csv_file, susceptible, infected, cumulative_infected, daily_infected, incubating, asymptomatic, 
        symptomatic, recovered, dead, daily_dead, hospitalized, breathing_issue, respirator, icu, parameters, people_tested,
        spreader, quarantined, symptomatic_tests, contact_trace_tests, extra_tests, positive_symptomatic_tests, positive_contact_trace_tests, positive_extra_tests):
    with open(csv_file, 'w', newline = '') as f:
        writer = csv.writer(f)
        l = []
        writer.writerow(l)
    
        l = []
        l.append('Day')
        l.append('Susceptible')
        l.append('Infected')
        l.append('Cumulative Infected')
        l.append('Daily Infected')
        l.append('Incubating')
        l.append('Asymptomatic')
        l.append('Symptomatic')
        l.append('Recovered')
        l.append('Dead')
        l.append('Daily Dead')
        l.append('Hospitalized')
        l.append('Breathing Issue')
        l.append('Respirator')
        l.append('ICU')
        l.append('Daily Tested')
        l.append('Spreader')
        l.append('Quarantined')
        l.append('Symptomatic Tests')
        l.append('Contact Trace Tests')
        l.append('Extra Tests')
        l.append('Positive Symptomatic Tests')
        l.append('Positive Contact Trace Tests')
        l.append('Positive Extra Tests')
        writer.writerow(l)

        # len used to iterate through every day
        for i in range(len(susceptible)):
            l = []
            l.append(i)
            l.append(susceptible[i])
            l.append(infected[i])
            l.append(cumulative_infected[i])
            l.append(daily_infected[i])
            l.append(incubating[i])
            l.append(asymptomatic[i])
            l.append(symptomatic[i])
            l.append(recovered[i])
            l.append(dead[i])
            l.append(daily_dead[i])
            l.append(hospitalized[i])
            l.append(breathing_issue[i])
            l.append(respirator[i])
            l.append(icu[i])
            l.append(people_tested[i])
            l.append(spreader[i])
            l.append(quarantined[i])
            l.append(symptomatic_tests[i])
            l.append(contact_trace_tests[i])
            l.append(extra_tests[i])
            l.append(positive_symptomatic_tests[i])
            l.append(positive_contact_trace_tests[i])
            l.append(positive_extra_tests[i])
            writer.writerow(l)
    f.close()

def updateCSV3(csv_file, class_person_infected):
    with open(csv_file, 'w', newline = '') as f:
        writer = csv.writer(f)
        l = []
        writer.writerow(l)
    
        l = []
        l.append('Day')
        for course in range(len(class_person_infected[0])):
            l.append(str(course))
        writer.writerow(l)

        # len used to iterate through every day
        for i in range(len(class_person_infected)):
            l = []
            l.append(i)
            for course in range(len(class_person_infected[0])):
                l.append(class_person_infected[i][course])
            writer.writerow(l)
    f.close()