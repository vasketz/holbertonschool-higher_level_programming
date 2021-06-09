#!/usr/bin/python3
"""
This is the tests of class Base
"""
import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """
    class unittest BaseTest
    """
    def test_id(self):
        """
        method test
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(21)
        self.assertEqual(b2.id, 21)
        b3 = Base(-22)
        self.assertEqual(b3.id, -22)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base("er")
        self.assertEqual(b5.id, "er")
        b6 = Base([1, 2, 3])
        self.assertEqual(b6.id, [1, 2, 3])
