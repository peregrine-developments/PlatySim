# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 18:39:13 2021

@author: Perry
"""
##-----------
## LIBRARIES
##-----------
import math
import csv

from core.vector import *
from core.quaternion import *
from sim.physics import *

from typing import List, Dict

##------------
## SIMULATION
##------------
running = True
simElapsedTime = 0.0
simDT = 0.01

testBody = AerodynamicRigidbody(mass = 10, pos = Vector3(0, 0, 1000), vel=Vector3(30, 20, 0), dragCoeff = lambda aoa : 0.1)

data : List[Dict[str, float]] = []

while running:
    testBody.update(simDT)
    data.append({"time": simElapsedTime, "x": testBody.pos.x, "y": testBody.pos.y, "z": testBody.pos.z,
                 "vx": testBody.vel.x, "vy": testBody.vel.y, "vz": testBody.vel.z,
                 "ax": testBody.lastAcc.x, "ay": testBody.lastAcc.y, "az": testBody.lastAcc.z})

    if testBody.pos.z < 0 or simElapsedTime >= 60:
        running = False

    simElapsedTime += simDT

print(f"Final sim time {simElapsedTime:.2f} seconds")

# write the values of data to a csv file
with open('data.csv', 'w', newline='') as csv_file:
    writer : csv.DictWriter = csv.DictWriter(csv_file, fieldnames=list(data[0].keys()))
    writer.writeheader()
    for row in data:
        writer.writerow(row)