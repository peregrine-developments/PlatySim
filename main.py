# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 18:39:13 2021

@author: Perry
"""
##-----------
## LIBRARIES
##-----------
import math

#import matplotlib.pyplot as plt
#from mpl_toolkits import mplot3d

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

testBody = Rigidbody(gravity = False)

data : List[Dict[str, float]] = [{"time": 0, "x": testBody.pos.x, "y": testBody.pos.y, "z": testBody.pos.z}]

while running:
    if simElapsedTime <= 4:
        testBody.applyForceLocal(Vector3(0, 0, 4), Vector3(0.5, 0.5, 0).normalized())

    testBody.update(simDT)
    data.append({"time": simElapsedTime, "x": testBody.pos.x, "y": testBody.pos.y, "z": testBody.pos.z})

    if simElapsedTime >= 8:
        testBody.gravity = True

    simElapsedTime += simDT

    if testBody.pos.z < 0 or simElapsedTime >= 12:
        running = False

print(f"Final sim time {simElapsedTime:.2f} seconds")

##----------
## GRAPHING
##----------
# xdata = []
# ydata = []
# zdata = []

# for point in data:
#     xdata.append(point["x"])
#     ydata.append(point["y"])
#     zdata.append(point["z"])

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# fig = ax.plot(xdata, ydata, zdata)
# plt.show()