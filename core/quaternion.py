# -*- coding: utf-8 -*-
"""
Created on Thu Sep 9 22:35:27 2021

@author: Perry
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Union, Tuple, Optional

from numbers import Number
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

        self.w = float(w)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    @classmethod
    def FromVector(cls, other : Vector3) -> Quaternion:
        """
        Construct a Quaternion object from a given Vector3

        Parameters
        ----------
        other : Vector3
            Vector3 to store in returned Quaternion

        Returns
        -------
        Quaternion
            Stored Vector3 in Quaternion form
        """
        return cls(0, other.x, other.y, other.z)

    @classmethod
    def FromEuler(cls, yaw : float, pitch : float, roll : float) -> Quaternion:
        """
        Construct a Quaternion object from a set of euler angles in radians

        Parameters
        ----------
        yaw : float
            Yaw component of the  euler angles
        pitch : float
            Pitch component of the euler angles
        roll : float
            Roll component of the euler angles

        Returns
        -------
        Quaternion
            Converted euler rotation in Quaternion form
        """
        cy = math.cos(yaw / 2)
        cp = math.cos(pitch / 2)
        cr = math.cos(roll / 2)

        sy = math.sin(yaw / 2)
        sp = math.sin(pitch / 2)
        sr = math.sin(roll / 2)

        return cls((cr * cp * cy) + (sr * sp * sy), (sr * cp * cy) - (cr * sp * sy), (cr * sp * cy) + (sr * cp * sy), (cr * cp * sy) - (sr * sp * cy))

    def ToEuler(self) -> Tuple[float, float, float]:
        """
        Convert a Quaternion object to a set of euler angles
        
        Returns
        -------
        Tuple[float, float, float]
            Euler rotation components in yaw, pitch, roll order
        """
        sinr_cosp = 2 * (self.w * self.x + self.y * self.z)
        cosr_cosp = 1 - 2 * (self.x * self.x + self.y * self.y)

        roll = math.atan2(sinr_cosp, cosr_cosp)

        sinp = 2 * (self.w * self.y - self.z * self.x)
        if abs(sinp) >= 1:
            pitch = math.copysign(math.pi / 2, sinp)
        else:
            pitch = math.asin(sinp)

        siny_cosp = 2 * (self.w * self.z + self.x * self.y)
        cosy_cosp = 1 - 2 * (self.y * self.y + self.z * self.z)
        yaw = math.atan2(siny_cosp, cosy_cosp)

        return yaw, pitch, roll

    @classmethod
    def FromRotationVector(cls, x : Union[float, Vector3], y : Optional[float] = None, z : Optional[float] = None) -> Quaternion:
        """
        Construct a Quaternion object from a given rotation vector

        Parameters
        ----------
        x : float OR Vector3
            If float, x component of vector, if Vector3, entire input vector
        y : float
            If x float, y component of vector
        z : float
            If x float, z component of vector

        Returns
        -------
        Quaternion
            Converted rotation vector in Quaternion form
        """
        if (isinstance(x, Vector3) and x == Vector3.Zero()) or (x == 0 and y == 0 and z == 0):
            return Quaternion.Zero()

        if isinstance(x, Vector3):
            return cls.FromAxisAngle(x.norm(), x.normalized())
        elif x is not None and y is not None and z is not None:
            vec = Vector3(x, y, z)
            return cls.FromAxisAngle(vec.norm(), vec.normalized())
        return NotImplemented

    def ToRotationVector(self) -> Vector3:
        """
        Convert a Quaternion object to a rotation vector
        
        Returns
        -------
        Vector3
            Representative rotation vector of Quaternion
        """
        angle, axis = self.ToAxisAngle()

        return axis * angle

    @classmethod
    def FromAxisAngle(cls, angle : float, x : Union[float, Vector3], y : Optional[float] = None, z : Optional[float] = None) -> Quaternion:
        """
        Construct a Quaternion object from a given axis-angle representation

        Parameters
        ----------
        angle : float
            Angle of the axis-angle representation
        x : float OR Vector3
            If float, x component of axis vector, if Vector3, entire input vector
        y : float
            If x float, y component of axis vector
        z : float
            If x float, z component of axis vector

        Returns
        -------
        Quaternion
            Converted axis-angle in Quaternion form
        """
        if angle == 0 or (isinstance(x, Vector3) and x == Vector3.Zero()) or (x == 0 and y == 0 and z == 0):
            return Quaternion.Zero()

        sa = math.sin(angle / 2)

        if isinstance(x, Vector3):
            return cls(math.cos(angle / 2), x.x * sa, x.y * sa, x.z * sa)
        elif x is not None and y is not None and z is not None:
            return cls(math.cos(angle / 2), x * sa, y * sa, z * sa)
        return NotImplemented

    def ToAxisAngle(self) -> Tuple[float, Vector3]:
        """
        Convert a Quaternion object to an axis-angle representation
        
        Returns
        -------
        Tuple[float, Vector3]
            Axis-angle representation in angle, axis order
        """
        angle = math.acos(self.w) * 2

        if angle == 0:
            return 0, Vector3.Zero()

        sa = math.sin(angle / 2)

        return angle, Vector3(self.x / sa, self.y / sa, self.z / sa).normalized()

    @classmethod
    def Zero(cls) -> Quaternion:
        """
        Return a Quaternion which does not rotate
        
        Returns
        -------
        Quaternion
            Zero-rotation quaternion
        """
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
        
        if isinstance(other, Quaternion):
            ret = Quaternion()

            ret.w = (self.w * other.w) - (self.x * other.x) - (self.y * other.y) - (self.z * other.z)
            ret.x = (self.w * other.x) + (self.x * other.w) + (self.y * other.z) - (self.z * other.y)
            ret.y = (self.w * other.y) - (self.x * other.z) + (self.y * other.w) + (self.z * other.x)
            ret.z = (self.w * other.z) + (self.x * other.y) - (self.y * other.x) + (self.z * other.w)

            return ret
        elif isinstance(other, Number):
            return Quaternion(self.w * float(other), self.x * float(other), self.y * float(other), self.z * float(other))
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

        if not isinstance(other, Number):
            return NotImplemented
        return Quaternion(self.w / float(other), self.x / float(other), self.y / float(other), self.z / float(other))

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
