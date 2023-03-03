#!/usr/bin/python3
"""Unittest for City class"""
import unittest
import os
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.cityInstance = City()
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
        """Test case for 'City' class attributes"""
        self.assertEqual(self.cityInstance.state_id, "")
        self.assertEqual(self.cityInstance.name, "")


if __name__ == "__main__":
    unittest.main()
