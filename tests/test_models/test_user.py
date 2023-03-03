#!/usr/bin/python3
"""Unittest for User class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def test_attrs(self):
        """Test case for 'User' class attributes"""
        userInstance = User()
        self.assertEqual(userInstance.email, "")
        self.assertEqual(userInstance.password, "")
        self.assertEqual(userInstance.first_name, "")
        self.assertEqual(userInstance.last_name, "")


if __name__ == "__main__":
    unittest.main()
