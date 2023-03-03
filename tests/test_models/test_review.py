#!/usr/bin/python3
"""Unittest for Review class"""
import unittest
import os
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.reviewInstance = Review()
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
        """Test case for 'Review' class attributes"""
        self.assertEqual(self.reviewInstance.place_id, "")
        self.assertEqual(self.reviewInstance.user_id, "")
        self.assertEqual(self.reviewInstance.text, "")


if __name__ == "__main__":
    unittest.main()
