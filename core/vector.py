# -*- coding: utf-8 -*-
"""
Created on Thu Sep 9 22:01:00 2021

@author: Perry
"""
from __future__ import annotations
from dataclasses import dataclass

from numbers import Number
import math

@dataclass
class Vector2:
    """
    A class to represent a two-dimensional vector

    ...

    Attributes
    ----------
    x : float
        x component of the vector
    y : float
        y component of the vector
    
    Methods
    -------
    norm():
        Calculates and returns the vector's length
    normalized():
        Calculates and returns a normalized representation of this vector (length = 1)
    dot():
        Calculates the dot product of this vector and another
    cross():
        Calculates the cross product (scalar) of this vector and another
    """

    x : float = 0
    y : float = 0

    def __init__(self, x : float = 0, y : float = 0) -> None:
        """
        Construct all necessary attributes for a Vector2 object

        Parameters
        ----------
        x : float
            x component of the vector
        y : float
            y component of the vector
        """

        self.x = float(x)
        self.y = float(y)

    @classmethod
    def Zero(cls) -> Vector2:
        return cls(0, 0)

    @classmethod
    def UnitX(cls) -> Vector2:
        return cls(1, 0)

    @classmethod
    def UnitY(cls) -> Vector2:
        return cls(0, 1)

    def __str__(self) -> str:
        """
        Return a simple string representation of a Vector2 object

        Returns
        -------
        str
            Simple string representation
        """

        return ''.join(["(", str(self.x), ",", str(self.y), ")"])
        
    def __repr__(self) -> str:
        """
        Return a comprehensive string representation of a Vector2 object

        Returns
        -------
        str
            Comprehensive string representation
        """
        
        return ''.join(["Vector2(", str(self.x), ",", str(self.y), ")"])

    def __eq__(self, other : object) -> bool:
        """
        Return the equality of two Vector2 objects

        Parameters
        ----------
        other : Vector2
            Vector2 for right-hand operand in equality

        Returns
        -------
        bool
            Equality of operands
        """

        if not isinstance(other, Vector2):
            return NotImplemented
        return ((self.x == other.x) and (self.y == other.y))

    def __ne__(self, other : object) -> bool:
        """
        Return the inequality of two Vector2 objects

        Parameters
        ----------
        other : Vector2
            Vector2 for right-hand operand in inequality

        Returns
        -------
        bool
            Inequality of operands
        """

        if not isinstance(other, Vector2):
            return NotImplemented
        return ((self.x != other.x) or (self.y != other.y))

    def __pos__(self) -> Vector2:
        """
        Return a positive Vector2 object

        Returns
        -------
        Vector2
            Positive vector
        """

        return Vector2(+self.x, +self.y)

    def __neg__(self) -> Vector2:
        """
        Return a negated Vector2 object

        Returns
        -------
        Vector2
            Negated vector
        """

        return Vector2(-self.x, -self.y)

    def __add__(self, other : Vector2) -> Vector2:
        """
        Return a sum of two Vector2 objects

        Parameters
        ----------
        other : Vector2
            Vector2 for right-hand operand in addition

        Returns
        -------
        Vector2
            Componentwise sum of operands
        """

        if not isinstance(other, Vector2):
            return NotImplemented
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other : Vector2) -> Vector2:
        """
        Return a minutend of two Vector2 objects

        Parameters
        ----------
        other : Vector2
            Vector2 for right-hand operand in subtraction

        Returns
        -------
        Vector2
            Componentwise minutend of operands
        """

        if not isinstance(other, Vector2):
            return NotImplemented
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other : float) -> Vector2:
        """
        Return a scalar multiplication of a Vector2 object

        Parameters
        ----------
        other : float
            Scalar value for right-hand operand in multiplication

        Returns
        -------
        Vector2
            Componentwise scalar multiplication of operands
        """

        if not isinstance(other, Number):
            return NotImplemented
        return Vector2(self.x * float(other), self.y * float(other))

    def __truediv__(self, other : float) -> Vector2:
        """
        Return a scalar division of a Vector2 object

        Parameters
        ----------
        other : float
            Scalar value for right-hand operand in division

        Returns
        -------
        Vector2
            Componentwise scalar division of operands
        """

        if not isinstance(other, Number):
            return NotImplemented
        return Vector2(self.x / float(other), self.y / float(other))

    def norm(self) -> float:
        """
        Calculate and return the length of a Vector2 object

        Returns
        -------
        int
            Calculated vector length
        """

        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def normalized(self) -> Vector2:
        """
        Calculate and return a normalized representation of a Vector2 object

        Returns
        -------
        Vector2
            Normalized vector representation
        """

        vecLen = self.norm()
        if vecLen == 0:
            return Vector2.Zero()
        return (self / vecLen)

    def dot(self, other : Vector2) -> float:
        """
        Calculate and return the dot product of this Vector2 and another

        Parameters
        ----------
        other : Vector2
            Vector2 for right-hand operand in dot product
        
        Returns
        -------
        float
            Resultant dot product
        """

        if not isinstance(other, Vector2):
            return NotImplemented
        return ((self.x * other.x) + (self.y * other.y))

    def cross(self, other : Vector2) -> float:
        """
        Calculate and return the cross product (scalar) of this Vector2 and another

        Parameters
        ----------
        other : Vector2
            Vector2 for right-hand operand in cross product
        
        Returns
        -------
        float
            Resultant cross product
        """

        if not isinstance(other, Vector2):
            return NotImplemented
        return ((self.x * other.y) - (self.y * other.x))

    def angle(self, other : Vector2) -> float:
        """
        Calculate and return the angle between this Vector2 and another

        Parameters
        ----------
        other : Vector2
            Vector2 for right-hand operand in angle calculation

        Returns
        -------
        float
            Calculated angle
        """

        if not isinstance(other, Vector2):
            return NotImplemented
        return math.acos(self.dot(other) / (self.norm() * other.norm()))

@dataclass
class Vector3:
    """
    A class to represent a three-dimensional vector

    ...

    Attributes
    ----------
    x : float
        x component of the vector
    y : float
        y component of the vector
    z : float
        z component of the vector
    
    Methods
    -------
    norm():
        Calculates and returns the vector's length
    normalized():
        Calculates and returns a normalized representation of this vector (length = 1)
    dot():it d
        Calculates the dot product of this vector and another
    cross():
        Calculates the cross product of this vector and another
    """

    x : float = 0
    y : float = 0
    z : float = 0

    def __init__(self, x : float = 0, y : float = 0, z : float = 0) -> None:
        """
        Construct all necessary attributes for a Vector3 object

        Parameters
        ----------
        x : float
            x component of the vector
        y : float
            y component of the vector
        z : float
            z component of the vector
        """

        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    @classmethod
    def Zero(cls) -> Vector3:
        return cls(0, 0, 0)

    @classmethod
    def UnitX(cls) -> Vector3:
        return cls(1, 0, 0)

    @classmethod
    def UnitY(cls) -> Vector3:
        return cls(0, 1, 0)
    
    @classmethod
    def UnitZ(cls) -> Vector3:
        return cls(0, 0, 1)

    def __str__(self) -> str:
        """
        Return a simple string representation of a Vector3 object

        Returns
        -------
        str
            Simple string representation
        """

        return ''.join(["(", str(self.x), ",",
            str(self.y), ",", str(self.z), ")"])
        
    def __repr__(self) -> str:
        """
        Return a comprehensive string representation of a Vector3 object

        Returns
        -------
        str
            Comprehensive string representation
        """
        
        return ''.join(["Vector3(", str(self.x), ",",
            str(self.y), ",", str(self.z), ")"])

    def __eq__(self, other : object) -> bool:
        """
        Return the equality of two Vector3 objects

        Parameters
        ----------
        other : Vector3
            Vector3 for right-hand operand in equality

        Returns
        -------
        bool
            Equality of operands
        """

        if not isinstance(other, Vector3):
            return NotImplemented
        return ((self.x == other.x) and (self.y == other.y) and (self.z == other.z))

    def __ne__(self, other : object) -> bool:
        """
        Return the inequality of two Vector3 objects

        Parameters
        ----------
        other : Vector3
            Vector3 for right-hand operand in inequality

        Returns
        -------
        bool
            Inequality of operands
        """

        if not isinstance(other, Vector3):
            return NotImplemented
        return ((self.x != other.x) or (self.y != other.y) or (self.z != other.z))

    def __pos__(self) -> Vector3:
        """
        Return a positive representation of a Vector3 object

        Returns
        -------
        Vector3
            Positive vector representation
        """

        return Vector3(+self.x, +self.y, +self.z)

    def __neg__(self) -> Vector3:
        """
        Return a negative representation of a Vector3 object

        Returns
        -------
        Vector3
            Negative vector representation
        """

        return Vector3(-self.x, -self.y, -self.z)

    def __add__(self, other : Vector3) -> Vector3:
        """
        Return a sum of two Vector3 objects

        Parameters
        ----------
        other : Vector3
            Vector3 for right-hand operand in addition

        Returns
        -------
        Vector3
            Componentwise sum of operands
        """

        if not isinstance(other, Vector3):
            return NotImplemented
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other : Vector3) -> Vector3:
        """
        Return a minutend of two Vector3 objects

        Parameters
        ----------
        other : Vector3
            Vector3 for right-hand operand in subtraction

        Returns
        -------
        Vector3
            Componentwise minutend of operands
        """

        if not isinstance(other, Vector3):
            return NotImplemented
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other : float) -> Vector3:
        """
        Return a scalar multiplication of a Vector3 object

        Parameters
        ----------
        other : float
            Scalar value for right-hand operand in multiplication

        Returns
        -------
        Vector3
            Componentwise scalar multiplication of operands
        """

        if not isinstance(other, Number):
            return NotImplemented
        return Vector3(self.x * float(other), self.y * float(other), self.z * float(other))

    def __truediv__(self, other : float) -> Vector3:
        """
        Return a scalar division of a Vector3 object

        Parameters
        ----------
        other : float
            Scalar value for right-hand operand in division

        Returns
        -------
        Vector3
            Componentwise scalar division of operands
        """

        if not isinstance(other, Number):
            return NotImplemented
        return Vector3(self.x / float(other), self.y / float(other), self.z / float(other))

    def norm(self) -> float:
        """
        Calculate and return the length of a Vector3 object

        Returns
        -------
        int
            Calculated vector length
        """

        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))

    def normalized(self) -> Vector3:
        """
        Calculate and return a normalized representation of a Vector3 object

        Returns
        -------
        Vector3
            Normalized vector representation
        """

        vecLen = self.norm()
        if vecLen == 0:
            return Vector3.Zero()
        return (self / vecLen)

    def dot(self, other : Vector3) -> float:
        """
        Calculate and return the dot product of this Vector3 and another

        Parameters
        ----------
        other : Vector3
            Vector3 for right-hand operand in dot product
        
        Returns
        -------
        float
            Resultant dot product
        """

        if not isinstance(other, Vector3):
            return NotImplemented
        return ((self.x * other.x) + (self.y * other.y) + (self.z * other.z))

    def cross(self, other : Vector3) -> Vector3:
        """
        Calculate and return the cross product (scalar) of this Vector3 and another

        Parameters
        ----------
        other : Vector3
            Vector3 for right-hand operand in cross product
        
        Returns
        -------
        Vector3
            Resultant cross product
        """

        if not isinstance(other, Vector3):
            return NotImplemented
        return Vector3((self.y * other.z) - (self.z * other.y), (self.z * other.x) - (self.x * other.z), (self.x * other.y) - (self.y * other.x))

    def angle(self, other : Vector3) -> float:
        """
        Calculate and return the angle between this Vector3 and another

        Parameters
        ----------
        other : Vector3
            Vector3 for right-hand operand in angle calculation

        Returns
        -------
        float
            Resultant angle
        """

        if not isinstance(other, Vector3):
            return NotImplemented
        return math.acos(self.dot(other) / (self.norm() * other.norm()))