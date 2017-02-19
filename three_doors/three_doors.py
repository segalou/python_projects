
# coding: utf-8

import random

stay_win, switch_win = 0, 0
sim_rounds = 10000

for i in range(sim_rounds):
    doors = {
        1: "sheep",
        2: "sheep",
        3: "sheep"
    } 

    doors[random.randint(1,3)] = 'car'
    choice = random.randint(1,3)
    while True:
        i = random.randint(1,3)
        if i <> choice and doors[i] == "sheep":
            doors.pop(i)
            break
    
    if doors[choice] == 'car':
        stay_win += 1.0
    else:
        switch_win += 1.0

print stay_win/sim_rounds
print switch_win/sim_rounds


