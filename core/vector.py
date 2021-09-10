# -*- coding: utf-8 -*-
"""
Created on Thu Sep 9 10:01:00 2021

@author: Perry
"""
import math
import numbers

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
    """

    def __init__(self, x, y):
        """
        Construct all necessary attributes for a Vector2 object

        Parameters
        ----------
        x : float
            x component of the vector
        y : float
            y component of the vector
        """

        if not isinstance(x, numbers.Number) or not isinstance(y, numbers.Number):
            raise TypeError

        self.x = x
        self.y = y

    def __str__(self):
        """
        Return a simple string representation of a Vector2 object

        Returns
        -------
        str
            Simple string representation
        """

        return ''.join(["(", str(self.x), ",", str(self.y), ")"])
        
    def __repr__(self):
        """
        Return a comprehensive string representation of a Vector2 object

        Returns
        -------
        str
            Comprehensive string representation
        """
        
        return ''.join(["Vector2(", str(self.x), ",", str(self.y), ")"])

    def __eq__(self, other):
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

        if isinstance(other, Vector2):
            return ((self.x == other.x) and (self.y == other.y))
        raise TypeError

    def __ne__(self, other):
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

        if isinstance(other, Vector2):
            return ((self.x != other.x) or (self.y != other.y))
        raise TypeError

    def __add__(self, other):
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

        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        raise TypeError

    def __sub__(self, other):
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

        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        raise TypeError

    def __mul__(self, other):
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

        if isinstance(other, numbers.Number):
            return Vector2(self.x * other, self.y * other)
        raise TypeError

    def __truediv__(self, other):
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

        if isinstance(other, numbers.Number):
            return Vector2(self.x / other, self.y / other)
        raise TypeError

    def norm(self):
        """
        Calculate and return the length of a Vector2 object

        Returns
        -------
        int
            Calculated vector length
        """

        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def normalized(self):
        """
        Calculate and return a normalized representation of a Vector2 object

        Returns
        -------
        Vector2
            Normalized vector representation
        """

        return self / self.norm()