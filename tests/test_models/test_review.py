#!/usr/bin/python3
"""Unittest for Review class"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_attrs(self):
        """Test case for 'Review' class attributes"""
        reviewInstance = Review()
        self.assertEqual(reviewInstance.place_id, "")
        self.assertEqual(reviewInstance.user_id, "")
        self.assertEqual(reviewInstance.text, "")


if __name__ == "__main__":
    unittest.main()
