from django.test import TestCase
from app.calc import add, subtrack


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test two numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """Test that values are subtracked and returned"""
        self.assertEqual(subtrack(5, 11), 6)
