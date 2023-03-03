#!/usr/bin/python3
"""Unittest for City class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def test_attrs(self):
        """Test case for 'City' class attributes"""
        cityInstance = City()
        self.assertEqual(cityInstance.state_id, "")
        self.assertEqual(cityInstance.name, "")


if __name__ == "__main__":
    unittest.main()
