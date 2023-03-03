#!/usr/bin/python3
"""Unittest for State class"""
import unittest
import os
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State class"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.stateInstance = State()
        try:
            os.rename("file.json", "test_file.json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        """Class method to close test's environment"""
        try:
            os.remove("file.json")
            os.rename("test_file.json", "file.json")
        except Exception:
            pass

    def test_attrs(self):
        """Test case for 'State' class attributes"""
        self.assertEqual(self.stateInstance.name, "")


if __name__ == "__main__":
    unittest.main()
