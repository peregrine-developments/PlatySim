# -*- coding: utf-8 -*-
"""
Created on Thu Sep 9 22:35:27 2021

@author: Perry
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Union, overload

import math

from .vector import *

@dataclass
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
    
    Factories
    ---------
    FromVector():
        Creates a Quaternion from a Vector3 object
    FromEuler():
        Creates a Quaternion from a set of euler angles
    FromAxisAngle():
        Creates a Quaternion from a given axis-angle representation

    Methods
    -------
    norm():
        Calculates and returns the quaternion's length
    normalized():
        Calculates and returns a normalized representation of this quaternion (length = 1)
    conj():
        Calculates and returns the quaternion's conjugate
    fractional():
        Returns a quaternion that rotates some fraction of the original
    """

    w : float = 0
    x : float = 0
    y : float = 0
    z : float = 0

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

        self.w = w
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def FromVector(cls, other : Vector3) -> Quaternion:
        return cls(0, other.x, other.y, other.z)

    @classmethod
    def FromEuler(cls, yaw : float, pitch : float, roll : float) -> Quaternion:
        cy = math.cos(yaw / 2)
        cp = math.cos(pitch / 2)
        cr = math.cos(roll / 2)

        sy = math.sin(yaw / 2)
        sp = math.sin(pitch / 2)
        sr = math.sin(roll / 2)

        return cls((cr * cp * cy) + (sr * sp * sy), (sr * cp * cy) - (cr * sp * sy), (cr * sp * cy) + (sr * cp * sy), (cr * cp * sy) - (sr * sp * cy))

    @classmethod
    def FromAxisAngle(cls, angle : float, x : Union[float, Vector3], y : float = None, z : float = None) -> Quaternion:
        if angle == 0 or (isinstance(x, Vector3) and x == Vector3.Zero()) or (x == 0 and y == 0 and z == 0):
            return Quaternion.Zero()

        sa = math.sin(angle / 2)

        if isinstance(x, Vector3):
            return cls(math.cos(angle / 2), x.x * sa, x.y * sa, x.z * sa)
        return cls(math.cos(angle / 2), x * sa, y * sa, z * sa)

    def ToAxisAngle(self) -> Vector3:
        angle = math.acos(self.w) * 2

        if angle == 0:
            return Vector3.Zero()

        sa = math.sin(angle / 2)

        return Vector3(self.x / sa, self.y / sa, self.z / sa).normalized() * angle

    @classmethod
    def Zero(cls) -> Quaternion:
        return cls(1, 0, 0, 0)

    def __str__(self) -> str:
        """
        Return a simple string representation of a Quaternion object

        Returns
        -------
        str
            Simple string representation
        """

        return ''.join(["(", str(self.w), ",", str(self.x), ",", str(self.y), ",", str(self.z), ")"])
        
    def __repr__(self) -> str:
        """
        Return a comprehensive string representation of a Quaternion object

        Returns
        -------
        str
            Comprehensive string representation
        """
        
        return ''.join(["Quaternion(", str(self.w), ",", str(self.x), ",", str(self.y), ",", str(self.z), ")"])

    def __eq__(self, other : object) -> bool:
        """
        Return the equality of two Quaternion objects

        Parameters
        ----------
        other : Quaternion
            Quaternion for right-hand operand in equality

        Returns
        -------
        bool
            Equality of operands
        """

        if not isinstance(other, Quaternion):
            return NotImplemented
        return ((self.w == other.w) and (self.x == other.x) and (self.y == other.y) and (self.z == other.z))

    def __ne__(self, other : object) -> bool:
        """
        Return the inequality of two Quaternion objects

        Parameters
        ----------
        other : Quaternion
            Quaternion for right-hand operand in inequality

        Returns
        -------
        bool
            Inequality of operands
        """

        if not isinstance(other, Quaternion):
            return NotImplemented
        return ((self.w != other.w) or (self.x != other.x) or (self.y != other.y) or (self.z != other.z))

    def __add__(self, other : Quaternion) -> Quaternion:
        """
        Return a sum of two Quaternion objects

        Parameters
        ----------
        other : Quaternion
            Quaternion for right-hand operand in addition

        Returns
        -------
        Quaternion
            Componentwise sum of operands
        """

        if not isinstance(other, Quaternion):
            return NotImplemented
        return Quaternion(self.w + other.w, self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other : Quaternion) -> Quaternion:
        """
        Return a minutend of two Quaternion objects

        Parameters
        ----------
        other : Quaternion
            Quaternion for right-hand operand in subtraction

        Returns
        -------
        Quaternion
            Componentwise minutend of operands
        """

        if not isinstance(other, Quaternion):
            return NotImplemented
        return Quaternion(self.w - other.w, self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other : Union[float, Quaternion]) -> Quaternion:
        """
        Return a multiplication of a Quaternion object

        Parameters
        ----------
        other : float, Quaternion
            Value for right-hand operand in multiplication

        Returns
        -------
        Quaternion
            Resultant multiplication of operands
        """
        if isinstance(other, float):
            return Quaternion(self.w * other, self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Quaternion):
            ret = Quaternion()

            ret.w = (self.w * other.w) - (self.x * other.x) - (self.y * other.y) - (self.z * other.z)
            ret.x = (self.w * other.x) + (self.x * other.w) + (self.y * other.z) - (self.z * other.y)
            ret.y = (self.w * other.y) - (self.x * other.z) + (self.y * other.w) + (self.z * other.x)
            ret.z = (self.w * other.z) + (self.x * other.y) - (self.y * other.x) + (self.z * other.w)

            return ret
        else:
            return NotImplemented

    def __rmul__(self, other : Vector3) -> Vector3:
        """
        Return a Quaternion rotation of a Vector3 object using right-hand multiplication

        Parameters
        ----------
        other : Vector3
            Value for left-hand operand in multiplication

        Returns
        -------
        Vector3
            Resultant rotation of Vector3 operand
        """

        if not isinstance(other, Vector3):
            return NotImplemented
        vec = Quaternion.FromVector(other)
        ret = self * vec * self.conj()
        return Vector3(ret.x, ret.y, ret.z)
    
    def __truediv__(self, other : float) -> Quaternion:
        """
        Return a scalar division of a Quaternion object

        Parameters
        ----------
        other : float
            Scalar value for right-hand operand in division

        Returns
        -------
        Quaternion
            Componentwise scalar division of operands
        """

        if not isinstance(other, float):
            return NotImplemented
        return Quaternion(self.w / other, self.x / other, self.y / other, self.z / other)

    def norm(self) -> float:
        """
        Calculate and return the length of a Vector3 object

        Returns
        -------
        int
            Calculated vector length
        """

        return math.sqrt(math.pow(self.w, 2) + math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))

    def normalized(self) -> Quaternion:
        """
        Calculate and return a normalized representation of a Quaternion object

        Returns
        -------
        Quaternion
            Normalized quaternion representation
        """

        quatLen = self.norm()
        if quatLen == 0:
            return Quaternion(0, 0, 0, 0)
        return (self / quatLen)
        
    def conj(self) -> Quaternion:
        """
        Calculate and return a conjugate representation of a Quaternion object

        Returns
        -------
        Quaternion
            Normalized quaternion representation
        """

        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def fractional(self, fraction : float) -> Quaternion:
        """
        Returns a quaternion that rotates some fraction of the original

        Parameters
        ----------
        fraction : float
            Fractional amount (0-1) to scale the Quaternion

        Returns
        -------
        Quaternion
            Fractional rotation Quaternion, normalized
        """
        return Quaternion((1 - fraction) + (self.w * fraction), self.x * fraction, self.y * fraction, self.z * fraction).normalized()
