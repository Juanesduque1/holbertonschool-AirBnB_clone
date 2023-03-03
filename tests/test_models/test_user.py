#!/usr/bin/python3
"""Unittest for User class"""
import unittest
import os
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.userInstance = User()
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
        """Test case for 'User' class attributes"""
        self.assertEqual(self.userInstance.email, "")
        self.assertEqual(self.userInstance.password, "")
        self.assertEqual(self.userInstance.first_name, "")
        self.assertEqual(self.userInstance.last_name, "")


if __name__ == "__main__":
    unittest.main()
