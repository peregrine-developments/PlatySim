# -*- coding: utf-8 -*-
"""
Created on Thu Sep 9 22:59:57 2021

@author: Perry
"""
from vector import *
import unittest
import operator

class TestVector2(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Vector2(0, 0).x, 0)
        self.assertEqual(Vector2(0, 0).y, 0)
        self.assertEqual(Vector2(10, 20).x, 10)
        self.assertEqual(Vector2(10, 20).y, 20)
        self.assertRaises(TypeError, Vector2, "0", 0)
        self.assertRaises(TypeError, Vector2, 0, "0")

    def test_str(self):
        self.assertEqual(str(Vector2(0, 0)), "(0,0)")
        self.assertEqual(str(Vector2(1, 1)), "(1,1)")
        self.assertEqual(str(Vector2(10, 20)), "(10,20)")

    def test_repr(self):
        self.assertEqual(repr(Vector2(0, 0)), "Vector2(0,0)")
        self.assertEqual(repr(Vector2(1, 1)), "Vector2(1,1)")
        self.assertEqual(repr(Vector2(10, 20)), "Vector2(10,20)")

    def test_eq(self):
        self.assertTrue(Vector2(0, 0) == Vector2(0, 0))
        self.assertTrue(Vector2(10, 20) == Vector2(10, 20))
        self.assertFalse(Vector2(0, 0) == Vector2(10, 20))
        self.assertRaises(TypeError, operator.eq, Vector2(0, 0), 0)
        self.assertRaises(TypeError, operator.eq, Vector2(0, 0), "0")

    def test_add(self):
        self.assertEqual(Vector2(0, 0) + Vector2(0, 0), Vector2(0, 0))
        self.assertEqual(Vector2(0, 0) + Vector2(2, 3), Vector2(2, 3))
        self.assertEqual(Vector2(2, 3) + Vector2(4, 5), Vector2(6, 8))
        self.assertEqual(Vector2(2, 3) + Vector2(4, 5), Vector2(4, 5) + Vector2(2, 3))
        self.assertRaises(TypeError, operator.add, Vector2(0, 0), 0)
        self.assertRaises(TypeError, operator.add, Vector2(0, 0), "0")

    def test_sub(self):
        self.assertEqual(Vector2(0, 0) - Vector2(0, 0), Vector2(0, 0))
        self.assertEqual(Vector2(0, 0) - Vector2(2, 3), Vector2(-2, -3))
        self.assertEqual(Vector2(2, 3) - Vector2(4, 5), Vector2(-2, -2))
        self.assertNotEqual(Vector2(2, 3) - Vector2(4, 5), Vector2(4, 5) - Vector2(2, 3))
        self.assertRaises(TypeError, operator.sub, Vector2(0, 0), 0)
        self.assertRaises(TypeError, operator.sub, Vector2(0, 0), "0")

    def test_mul(self):
        self.assertEqual(Vector2(0, 0) * 0, Vector2(0, 0))
        self.assertEqual(Vector2(0, 0) * 2, Vector2(0, 0))
        self.assertEqual(Vector2(1, 2) * 3, Vector2(3, 6))
        self.assertNotEqual(Vector2(1, 1) * 2, Vector2(1, 1))
        self.assertRaises(TypeError, operator.mul, Vector2(0, 0), "0")
        self.assertRaises(TypeError, operator.mul, Vector2(0, 0), Vector2(0, 0))

    def test_div(self):
        self.assertEqual(Vector2(0, 0) / 1, Vector2(0, 0))
        self.assertEqual(Vector2(1, 1) / 1, Vector2(1, 1))
        self.assertEqual(Vector2(2, 2) / 2, Vector2(1, 1))
        self.assertNotEqual(Vector2(3, 3) / 2, Vector2(3, 3))
        self.assertRaises(TypeError, operator.truediv, Vector2(0, 0), "0")
        self.assertRaises(ZeroDivisionError, operator.truediv, Vector2(1, 1), 0)

    def test_norm(self):
        self.assertEqual(Vector2(0, 0).norm(), 0)
        self.assertEqual(Vector2(0, 1).norm(), 1)
        self.assertEqual(Vector2(2, 0).norm(), 2)
        self.assertEqual(Vector2(3, 4).norm(), 5)

    def test_normalized(self):
        self.assertEqual(Vector2(0, 1).normalized(), Vector2(0, 1))
        self.assertEqual(Vector2(2, 0).normalized(), Vector2(1, 0))
        self.assertEqual(Vector2(3, 4).normalized(), Vector2(3/5, 4/5))
        self.assertRaises(ZeroDivisionError, Vector2.normalized, Vector2(0, 0))

    def test_dot(self):
        self.assertEqual(Vector2(0, 0).dot(Vector2(0, 0)), 0)
        self.assertEqual(Vector2(0, 0).dot(Vector2(1, 1)), 0)
        self.assertEqual(Vector2(1, 1).dot(Vector2(1, 1)), 2)
        self.assertEqual(Vector2(1, 2).dot(Vector2(3, 4)), 11)
        self.assertRaises(TypeError, Vector2(0, 0).cross, 0)
    
    def test_cross(self):
        self.assertEqual(Vector2(0, 0).cross(Vector2(0, 0)), 0)
        self.assertEqual(Vector2(0, 0).cross(Vector2(1, 1)), 0)
        self.assertEqual(Vector2(1, 0).cross(Vector2(0, 1)), 1)
        self.assertEqual(Vector2(1, 2).cross(Vector2(3, 4)), -2)
        self.assertRaises(TypeError, Vector2(0, 0).cross, 0)

unittest.main(argv=[''],verbosity=2, exit=False)