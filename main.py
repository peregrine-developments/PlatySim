# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 18:39:13 2021

@author: Perry
"""

import math

from core.vector import *
from core.quaternion import *
from sim.physics import Rigidbody

running = True

testBody = Rigidbody()

simElapsedTime = 0
simDT = 0.01

while running:
    print(f"{testBody.pos.x:.4f}, {testBody.pos.z:.4f}")

    if simElapsedTime <= 4:
        testBody.applyForceCoGLocal(Vector3(0, 0, 15))

    testBody.update(simDT)

    simElapsedTime += simDT

    if(testBody.pos.z < 0):
        running = False