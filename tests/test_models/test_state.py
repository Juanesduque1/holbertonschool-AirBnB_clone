#!/usr/bin/python3
"""Unittest for State class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def test_attrs(self):
        """Test case for 'State' class attributes"""
        stateInstance = State()
        self.assertEqual(stateInstance.name, "")


if __name__ == "__main__":
    unittest.main()
