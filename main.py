# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 18:39:13 2021

@author: Perry
"""

import math

from core.vector import *
from core.quaternion import *

unit = Quaternion(1, 0, 0, 0)

vector = Vector3(9.8, 0, 0)

rotation_aa = Quaternion.FromAxisAngle(math.pi / 2, 0, 1, 0)
rotation_euler = Quaternion.FromEuler(0, math.pi / 2, 0)

print(vector * rotation_aa)
print(vector * rotation_euler)