#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Prog1 import mul

class TestSum(unittest.TestCase):
    def test_list_int1(self):
        """
        Test case to add two numbers
        """
        data = [2, 3]
        result = mul(data)
        self.assertEqual(result, 6)
    def test_list_int2(self):
        """
        Test case to add two numbers
        """
        data = [0, 30]
        result = mul(data)
        self.assertEqual(result, 0)
    def test_list_int3(self):
        """
        Test case to add two numbers
        """
        data = [2,1]
        result = mul(data)
        self.assertEqual(result, 2)
    def test_list_int4(self):
        """
        Test case to add two numbers
        """
        data = [2, 3]
        result = mul(data)
        self.assertEqual(result, 6)
    def test_list_int5(self):
        """
        Test case to add two numbers
        """
        data = [0, 30]
        result = mul(data)
        self.assertEqual(result, 0)
    def test_list_int6(self):
        """
        Test case to add two numbers
        """
        data = [2,1]
        result = mul(data)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
