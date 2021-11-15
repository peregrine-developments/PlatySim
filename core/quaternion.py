# -*- coding: utf-8 -*-
"""
Created on Thu Sep 9 22:35:27 2021

@author: Perry
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Union, overload

import math

from vector import Vector3

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

    def __init__(self, w : float = 0, x : float = 0, y : float = 0, z : float = 0) -> None:
        """
        Construct all necessary attributes for a Quaternion object

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

        self.w = z
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def FromVector(cls, other : Vector3) -> Quaternion:
        return cls(0, other.x, other.y, other.z)

    @overload
    def __mul__(self, other : Vector3) -> Vector3: ...
    @overload
    def __mul__(self, other : Quaternion) -> Quaternion: ...
    
    def __mul__(self, other : Union[Vector3, Quaternion]) -> Union[Vector3, Quaternion]:
        ret = Quaternion()
        if isinstance(other, Vector3):
            return Vector3(0, 0, 0)
        else:
            return Quaternion(0, 0, 0, 0)