"""
Tests count
"""
import unittest

from count import Ten

class TestCount(unittest.TestCase):
    def setUp(self):
        self.res = Ten()
    def test_positive_a(self):
        self.assertEqual(7, self.res.summ(5,2))
    def test_positive_b(self):
        self.assertEqual(10, self.res.summ(5,5))
    def test_positive(self):
        self.assertEqual(1, self.res.summ(0,1))
    def test_n(self):
        self.assertEqual(11, self.res.summ(10,1))
    def test_n_a(self):
        self.assertEqual(11, self.res.summ(9,2))
if __name__== '__main__':
    unittest.main()
