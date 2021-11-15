# -*- coding: utf-8 -*-
"""
Created on Thu Sep 9 22:35:27 2021

@author: Perry
"""
from __future__ import annotations

import math

class Quaternion:
    """
    A class to represent a quaternion

    ...

    Attributes
    ----------
    w : float
        real component of the quaternion
    x : float
        x imaginary component of the quaternion
    y : float
        y imaginary component of the quaternion
    z : float
        z imaginary component of the quaternion
    
    Methods
    -------
    norm():
        Calculates and returns the quaternion's length
    normalized():
        Calculates and returns a normalized representation of this quaternion (length = 1)
    conjugate():
        Calculates and returns the quaternion's conjugate
    
    """

    def __init__(self, w : float, x : float, y : float, z : float) -> None:
        """
        Construct all necessary attributes for a Vector2 object

        Parameters
        ----------
        w : float
            real component of the quaternion
        x : float
            x imaginary component of the quaternion
        y : float
            y imaginary component of the quaternion
        z : float
            z imaginary component of the quaternion
        """

        
        self.x = x
        self.y = y