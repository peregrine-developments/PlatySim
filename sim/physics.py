# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 13:11:44 2021

@author: Perry
"""

import math

from core.vector import *
from core.quaternion import *

@dataclass
class Rigidbody:
    """
    A class to represent a rigidbody object in three-dimensional space

    ...

    Attributes
    ----------
    mass : float
        Mass of the rigidbody (in kg)
    pos : Vector3
        Position of the rigidbody's CoG in space
    vel : Vector3
        Velocity of the rigidbody's CoG
    ori : Quaternion
        Rotation of the rigidbody about its CoG
    gravity : bool
        Whether or not to apply gravity to this rigidbody
    acc : Vector3
        Translational acceleration of the rigidbody's CoG
    
    Methods
    -------
    applyForce():
        Applies a force (in N) through the rigidbody's CoG
    update():
        Updates the rigidbody with a given timestep
    """

    mass : float = 1
    pos : Vector3 = Vector3(0, 0, 0)
    vel : Vector3 = Vector3(0, 0, 0)
    ori : Quaternion = Quaternion(1, 0, 0, 0)
    gravity : bool = True
    acc : Vector3 = Vector3(0, 0, 0)

    def __init__(self, mass : float = 1, pos : Vector3 = Vector3(0, 0, 0), vel : Vector3 = Vector3(0, 0, 0), ori : Quaternion = Quaternion(1, 0, 0, 0)) -> None:
        """
        Construct all necessary attributes for a Rigidbody object

        Parameters
        ----------
        mass : float
            Mass of the rigidbody (in kg)
        pos : Vector3
            Position of the rigidbody's CoG in space
        vel : Vector3
            Velocity of the rigidbody's CoG
        ori : Quaternion
            Rotation of the rigidbody about its CoG
        """

        self.mass = mass
        self.pos = pos
        self.vel = vel
        self.ori = ori

    