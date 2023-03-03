#!/usr/bin/python3
"""Unittest for Amenity class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def test_attrs(self):
        """Test case for 'Amenity' class attributes"""
        amenityInstance = Amenity()
        self.assertEqual(amenityInstance.name, "")


if __name__ == "__main__":
    unittest.main()
