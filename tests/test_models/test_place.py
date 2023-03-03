#!/usr/bin/python3
"""Unittest for 'Place' class"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for 'Place' class"""

    def test_attrs(self):
        """Test case for 'Place' class attributes"""
        placeInstance = Place()
        self.assertEqual(placeInstance.city_id, "")
        self.assertEqual(placeInstance.user_id, "")
        self.assertEqual(placeInstance.name, "")
        self.assertEqual(placeInstance.description, "")
        self.assertEqual(placeInstance.number_rooms, 0)
        self.assertEqual(placeInstance.number_bathrooms, 0)
        self.assertEqual(placeInstance.max_guest, 0)
        self.assertEqual(placeInstance.price_by_night, 0)
        self.assertEqual(placeInstance.latitude, 0.0)
        self.assertEqual(placeInstance.longitude, 0.0)
        self.assertEqual(placeInstance.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
