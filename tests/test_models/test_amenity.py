#!/usr/bin/python3
"""Unittest for Amenity class"""
import unittest
import os
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.amenityInstance = Amenity()
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
        """Test case for 'Amenity' class attributes"""
        self.assertEqual(self.amenityInstance.name, "")


if __name__ == "__main__":
    unittest.main()
