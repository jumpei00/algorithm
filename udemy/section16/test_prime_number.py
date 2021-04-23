import unittest

from udemy.section16.prime_number import eratostenes
from udemy.section16.prime_number import is_prime


class TestPrimeNumber(unittest.TestCase):
    def setUp(self):
        self.nums = eratostenes(50)

    def test_is_prime_ok(self):
        for num in self.nums:
            self.assertTrue(is_prime(num), msg=num)

    def test_is_prime_no(self):
        for num in [1, 4, 6, 8, 12, 14]:
            self.assertFalse(is_prime(num))

    def test_is_prime_negative(self):
        self.assertFalse(is_prime(-1))

    def test_is_prime_string(self):
        with self.assertRaises(TypeError) as cm:
            is_prime('string')
            print(cm)
