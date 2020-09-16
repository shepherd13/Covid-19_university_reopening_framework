 # -*- coding: utf-8 -*-
import random
import numpy as np

# States: Dead(-2), Recovered (-1), Susceptible (0), Incubating (1), Asymptomatic (2), Symptomatic (3)
# Hospitalized States: Hospitalized (4), Breathing Difficulty (5), Respirator (6), ICU (7)

# Infection Transfer Model
# Processes visit, returns 1 if person got infected else 0
def updatePerson(day, person, location, score, state, parameters):
    # asymptomatic infected state
    if (state[day, person] == 2):
        # person leaves infection with param probability
        if (random.choices([0, 1], [1.0 - parameters['Leave Infection Rate'], parameters['Leave Infection Rate']])[0] == 1):
            score[location] += np.random.gamma(parameters['Infectiousness Shape'], (parameters['Infectiousness Mean'] / parameters['Infectiousness Shape']), 1)  # infectiousness follows gamma distribution

    # symptomatic infected state with some param probability of voltunary quarantining
    elif ((state[day, person] == 3) and (random.choices([0, 1], [parameters['Symptomatic Quarantine Rate'], 1.0 - parameters['Symptomatic Quarantine Rate']])[0] == 1)):
        # person leaves infection with param probability
        if (random.choices([0, 1], [1.0 - parameters['Leave Infection Rate'], parameters['Leave Infection Rate']])[0] == 1):
            score[location] += np.random.gamma(parameters['Infectiousness Shape'], (parameters['Infectiousness Mean'] / parameters['Infectiousness Shape']), 1) * parameters['Symptomatic Infection']  # symptomatic people are more infectious

    # susceptible state
    elif (state[day, person] == 0):
        infecP = score[location] / parameters['Threshold']  # probability of being infected

        # if over 100% chance of infection
        if (infecP > 1.0):
            infecP = 1.0                 # prevents error with random.choices function
            score[location] = parameters['Threshold']  # infection score has a max score of threshold (meaning 100% chance of infection)

        # probability roll to determine if person gets infected
        if (random.choices([0, 1], [1.0 - infecP, infecP])[0] == 1):
            state[day, person] = 1   # infected, incubating
            return 1
    return 0