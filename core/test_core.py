# -*- coding: utf-8 -*-
"""
Created on Thu Sep 9 22:59:57 2021

@author: Perry
"""
from .vector import *
from .quaternion import *
import unittest
import operator

class TestVector2(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Vector2(0, 0).x, 0)
        self.assertEqual(Vector2(0, 0).y, 0)
        self.assertEqual(Vector2(10, 20).x, 10)
        self.assertEqual(Vector2(10, 20).y, 20)

    def test_str(self):
        self.assertEqual(str(Vector2(0, 0)), "(0.0,0.0)")
        self.assertEqual(str(Vector2(1, 1)), "(1.0,1.0)")
        self.assertEqual(str(Vector2(10, 20)), "(10.0,20.0)")

    def test_repr(self):
        self.assertEqual(repr(Vector2(0, 0)), "Vector2(0.0,0.0)")
        self.assertEqual(repr(Vector2(1, 1)), "Vector2(1.0,1.0)")
        self.assertEqual(repr(Vector2(10, 20)), "Vector2(10.0,20.0)")

    def test_eq(self):
        self.assertTrue(Vector2(0, 0) == Vector2(0, 0))
        self.assertTrue(Vector2(10, 20) == Vector2(10, 20))
        self.assertFalse(Vector2(0, 0) == Vector2(10, 20))

    def test_neq(self):
        self.assertFalse(Vector2(0, 0) != Vector2(0, 0))
        self.assertFalse(Vector2(10, 20) != Vector2(10, 20))
        self.assertTrue(Vector2(0, 0) != Vector2(10, 20))

    def test_add(self):
        self.assertEqual(Vector2(0, 0) + Vector2(0, 0), Vector2(0, 0))
        self.assertEqual(Vector2(0, 0) + Vector2(2, 3), Vector2(2, 3))
        self.assertEqual(Vector2(2, 3) + Vector2(4, 5), Vector2(6, 8))
        self.assertEqual(Vector2(2, 3) + Vector2(4, 5), Vector2(4, 5) + Vector2(2, 3))

    def test_sub(self):
        self.assertEqual(Vector2(0, 0) - Vector2(0, 0), Vector2(0, 0))
        self.assertEqual(Vector2(0, 0) - Vector2(2, 3), Vector2(-2, -3))
        self.assertEqual(Vector2(2, 3) - Vector2(4, 5), Vector2(-2, -2))
        self.assertNotEqual(Vector2(2, 3) - Vector2(4, 5), Vector2(4, 5) - Vector2(2, 3))

    def test_mul(self):
        self.assertEqual(Vector2(0, 0) * 0, Vector2(0, 0))
        self.assertEqual(Vector2(0, 0) * 2, Vector2(0, 0))
        self.assertEqual(Vector2(1, 2) * 3, Vector2(3, 6))
        self.assertNotEqual(Vector2(1, 1) * 2, Vector2(1, 1))

    def test_div(self):
        self.assertEqual(Vector2(0, 0) / 1, Vector2(0, 0))
        self.assertEqual(Vector2(1, 1) / 1, Vector2(1, 1))
        self.assertEqual(Vector2(2, 2) / 2, Vector2(1, 1))
        self.assertNotEqual(Vector2(3, 3) / 2, Vector2(3, 3))
        self.assertRaises(ZeroDivisionError, operator.truediv, Vector2(1, 1), 0)

    def test_norm(self):
        self.assertEqual(Vector2(0, 0).norm(), 0)
        self.assertEqual(Vector2(1, 0).norm(), 1)
        self.assertEqual(Vector2(0, 2).norm(), 2)
        self.assertEqual(Vector2(3, 4).norm(), 5)

    def test_normalized(self):
        self.assertEqual(Vector2(1, 0).normalized(), Vector2(1, 0))
        self.assertEqual(Vector2(0, 2).normalized(), Vector2(0, 1))
        self.assertEqual(Vector2(3, 4).normalized(), Vector2(3/5, 4/5))
        self.assertEqual(Vector2(0, 0).normalized(), Vector2.Zero())

    def test_dot(self):
        self.assertEqual(Vector2(0, 0).dot(Vector2(0, 0)), 0)
        self.assertEqual(Vector2(0, 0).dot(Vector2(1, 1)), 0)
        self.assertEqual(Vector2(1, 1).dot(Vector2(1, 1)), 2)
        self.assertEqual(Vector2(1, 2).dot(Vector2(3, 4)), 11)
    
    def test_cross(self):
        self.assertEqual(Vector2(0, 0).cross(Vector2(0, 0)), 0)
        self.assertEqual(Vector2(0, 0).cross(Vector2(1, 1)), 0)
        self.assertEqual(Vector2(1, 0).cross(Vector2(0, 1)), 1)
        self.assertEqual(Vector2(1, 2).cross(Vector2(3, 4)), -2)

class TestVector3(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Vector3(0, 0, 0).x, 0)
        self.assertEqual(Vector3(0, 0, 0).y, 0)
        self.assertEqual(Vector3(0, 0, 0).z, 0)
        self.assertEqual(Vector3(10, 20, 30).x, 10)
        self.assertEqual(Vector3(10, 20, 30).y, 20)
        self.assertEqual(Vector3(10, 20, 30).z, 30)

    def test_str(self):
        self.assertEqual(str(Vector3(0, 0, 0)), "(0.0,0.0,0.0)")
        self.assertEqual(str(Vector3(1, 1, 1)), "(1.0,1.0,1.0)")
        self.assertEqual(str(Vector3(10, 20, 30)), "(10.0,20.0,30.0)")

    def test_repr(self):
        self.assertEqual(repr(Vector3(0, 0, 0)), "Vector3(0.0,0.0,0.0)")
        self.assertEqual(repr(Vector3(1, 1, 1)), "Vector3(1.0,1.0,1.0)")
        self.assertEqual(repr(Vector3(10, 20, 30)), "Vector3(10.0,20.0,30.0)")

    def test_eq(self):
        self.assertTrue(Vector3(0, 0, 0) == Vector3(0, 0, 0))
        self.assertTrue(Vector3(10, 20, 30) == Vector3(10, 20, 30))
        self.assertFalse(Vector3(0, 0, 0) == Vector3(10, 20, 30))

    def test_neq(self):
        self.assertFalse(Vector3(0, 0, 0) != Vector3(0, 0, 0))
        self.assertFalse(Vector3(10, 20, 30) != Vector3(10, 20, 30))
        self.assertTrue(Vector3(0, 0, 0) != Vector3(10, 20, 30))

    def test_add(self):
        self.assertEqual(Vector3(0, 0, 0) + Vector3(0, 0, 0), Vector3(0, 0, 0))
        self.assertEqual(Vector3(0, 0, 0) + Vector3(2, 3, 4), Vector3(2, 3, 4))
        self.assertEqual(Vector3(2, 3, 4) + Vector3(4, 5, 6), Vector3(6, 8, 10))
        self.assertEqual(Vector3(2, 3, 4) + Vector3(4, 5, 6), Vector3(4, 5, 6) + Vector3(2, 3, 4))

    def test_sub(self):
        self.assertEqual(Vector3(0, 0, 0) - Vector3(0, 0, 0), Vector3(0, 0, 0))
        self.assertEqual(Vector3(0, 0, 0) - Vector3(2, 3, 4), Vector3(-2, -3, -4))
        self.assertEqual(Vector3(2, 3, 4) - Vector3(4, 5, 6), Vector3(-2, -2, -2))
        self.assertNotEqual(Vector3(2, 3, 4) - Vector3(4, 5, 6), Vector3(4, 5, 6) - Vector3(2, 3, 4))

    def test_mul(self):
        self.assertEqual(Vector3(0, 0, 0) * 0, Vector3(0, 0, 0))
        self.assertEqual(Vector3(0, 0, 0) * 2, Vector3(0, 0, 0))
        self.assertEqual(Vector3(1, 2, 3) * 3, Vector3(3, 6, 9))
        self.assertNotEqual(Vector3(1, 1, 1) * 2, Vector3(1, 1, 1))

    def test_div(self):
        self.assertEqual(Vector3(0, 0, 0) / 1, Vector3(0, 0, 0))
        self.assertEqual(Vector3(1, 1, 1) / 1, Vector3(1, 1, 1))
        self.assertEqual(Vector3(2, 2, 2) / 2, Vector3(1, 1, 1))
        self.assertNotEqual(Vector3(3, 3, 3) / 2, Vector3(3, 3, 3))
        self.assertRaises(ZeroDivisionError, operator.truediv, Vector3(1, 1, 1), 0)

    def test_norm(self):
        self.assertEqual(Vector3(0, 0, 0).norm(), 0)
        self.assertEqual(Vector3(1, 0, 0).norm(), 1)
        self.assertEqual(Vector3(0, 2, 0).norm(), 2)
        self.assertEqual(Vector3(0, 0, 3).norm(), 3)
        self.assertEqual(Vector3(2, 3, 6).norm(), 7)

    def test_normalized(self):
        self.assertEqual(Vector3(1, 0, 0).normalized(), Vector3(1, 0, 0))
        self.assertEqual(Vector3(0, 2, 0).normalized(), Vector3(0, 1, 0))
        self.assertEqual(Vector3(0, 0, 3).normalized(), Vector3(0, 0, 1))
        self.assertEqual(Vector3(2, 3, 6).normalized(), Vector3(2/7, 3/7, 6/7))
        self.assertEqual(Vector3(0, 0, 0).normalized(), Vector3.Zero())

    def test_dot(self):
        self.assertEqual(Vector3(0, 0, 0).dot(Vector3(0, 0, 0)), 0)
        self.assertEqual(Vector3(0, 0, 0).dot(Vector3(1, 1, 1)), 0)
        self.assertEqual(Vector3(1, 1, 1).dot(Vector3(1, 1, 1)), 3)
        self.assertEqual(Vector3(1, 2, 3).dot(Vector3(4, 5, 6)), 32)
    
    def test_cross(self):
        self.assertEqual(Vector3(0, 0, 0).cross(Vector3(0, 0, 0)), Vector3(0, 0, 0))
        self.assertEqual(Vector3(0, 0, 0).cross(Vector3(1, 1, 1)), Vector3(0, 0, 0))
        self.assertEqual(Vector3(1, 0, 0).cross(Vector3(0, 0, 1)), Vector3(0, -1, 0))
        self.assertEqual(Vector3(1, 2, 3).cross(Vector3(4, 5, 6)), Vector3(-3, 6, -3))

unittest.main(argv=[''],verbosity=2, exit=False)