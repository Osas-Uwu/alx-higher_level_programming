iii#!/usr/bin/python3 # osariemen uwuilekhue j <uwuilekhue.osariemen@gmail.com>
# software engineering ALX courses
"""This module defines unittests for base.py.
"""

import os
import unittest
from models.base import base
from models.rectangle import rectangle
from models.square import square


class TestBase_instantiation(unittest.Testcase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)

