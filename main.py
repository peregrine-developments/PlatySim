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
from sim.physics import Rigidbody

from typing import List, Dict

##------------
## SIMULATION
##------------
running = True
simElapsedTime = 0.0
simDT = 0.01

testBody = Rigidbody()

data : List[Dict[str, float]] = [{"time": 0, "x": testBody.pos.x, "y": testBody.pos.y, "z": testBody.pos.z}]

while running:
    testBody.applyForceCoMLocal(Vector3(0, 0, 9.8))

    testBody.update(simDT)
    data.append({"time": simElapsedTime, "x": testBody.pos.x, "y": testBody.pos.y, "z": testBody.pos.z})

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