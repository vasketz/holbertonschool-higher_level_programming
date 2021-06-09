#!/usr/bin/python3
"""
This is the test_rectangle module
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    this is the test class
    """
    def test_rectangle(self):
        """
        function to test clas rectangle
        """
        r1 = Rectangle(10, 2)
        self.assertTrue(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(8, 15)
        self.assertTrue(r2.id, 2)
        self.assertEqual(r2.width, 8)
        self.assertEqual(r2.height, 15)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        r3 = Rectangle(8, 15, 5, 4, 6)
        self.assertEqual(r3.id, 6)
        self.assertEqual(r3.width, 8)
        self.assertEqual(r3.height, 15)
        self.assertEqual(r3.x, 5)
        self.assertEqual(r3.y, 4)
        
    def test_ErrorType(self):
        r = Rectangle("x", 2)
        self.assertRaises(TypeError, r.width)
        
    def test_ErrorValue(self):
        r1 = Rectangle(-0, 2)
        self.assertRaises(ValueError, r1.width)
        r2 = Rectangle(8, 15, -5, 4, 6)
        self.assertRaises(ValueError, r2.x)
        
    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)