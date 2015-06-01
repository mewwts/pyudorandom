import unittest
from pyudorandom import pyudorandom, bin_gcd

class Tests(unittest.TestCase):

    def test_generation_with_odd_number(self):
        n = 45
        elements = set(range(n))
        generated = set([])
        for i in pyudorandom(n):
            generated.add(i)
        self.assertEqual(generated, elements)

    def test_generation_with_even_number(self):
        n = 24
        elements = set(range(n))
        generated = set([])
        for i in pyudorandom(n):
            generated.add(i)
        self.assertEqual(generated, elements)

    def test_bin_gcd_simple(self):
        self.assertEqual(bin_gcd(4, 3), 1)

    def test_bin_gcd_hard(self):
        self.assertEqual(bin_gcd(54614, 12312), 2)

if __name__ == '__main__':
    unittest.main()

