#!/usr/bin/python3
"""Unittest for 'Place' class"""
import unittest
import os
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for 'Place' class"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.placeInstance = Place()
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
        """Test case for 'Place' class attributes"""
        self.assertEqual(self.placeInstance.city_id, "")
        self.assertEqual(self.placeInstance.user_id, "")
        self.assertEqual(self.placeInstance.name, "")
        self.assertEqual(self.placeInstance.description, "")
        self.assertEqual(self.placeInstance.number_rooms, 0)
        self.assertEqual(self.placeInstance.number_bathrooms, 0)
        self.assertEqual(self.placeInstance.max_guest, 0)
        self.assertEqual(self.placeInstance.price_by_night, 0)
        self.assertEqual(self.placeInstance.latitude, 0.0)
        self.assertEqual(self.placeInstance.longitude, 0.0)
        self.assertEqual(self.placeInstance.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
