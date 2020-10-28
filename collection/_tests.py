# 1. GCD test result

import unittest
from gcd import gcd

class TestGCD(unittest.TestCase):

    def test_result(self):
        self.assertEqual(gcd(200, 120), 40)
        self.assertEqual(gcd(160, 132), 4)
        self.assertEqual(gcd(200, 100), 100)
        self.assertEqual(gcd(13, 4), 1)