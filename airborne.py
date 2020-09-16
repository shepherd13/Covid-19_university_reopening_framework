 # -*- coding: utf-8 -*-
import math

# returns probability of getting infected by airborne infection
# pulmonary ventilation rate is in (m3/s)
# quanta rate is in (quanta/h), hard to calculate
# time is the number of hours
# room ventilation rate is in (AC/h)
# room volume is in (m3)
def airborneProb(time, num_infected, mask, room_volume, room_vent_rate, mask_efficiency, pulm_vent_rate=0.48):
    # if wearing mask
    if mask:
        return 1.0 - math.exp(-(num_infected * (pulm_vent_rate * (1.0 - mask_efficiency)) * time) / (room_vent_rate * room_volume))

    # if not wearing mask
    else:
        return 1.0 - math.exp(-(num_infected * pulm_vent_rate * time) / (room_vent_rate * room_volume))


def diffProb(time, num_infected, mask, room_volume, room_vent_rate, mask_efficiency, pulm_vent_rate=0.48):
    # if wearing mask
    if mask:
        return (num_infected * (pulm_vent_rate * (1.0 - mask_efficiency)) * time) / (room_vent_rate * room_volume)

    # if not wearing mask
    else:
        return (num_infected * pulm_vent_rate * time) / (room_vent_rate * room_volume)