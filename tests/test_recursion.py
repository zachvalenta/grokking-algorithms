import unittest

import src.recursion as r


class TestRecursion(unittest.TestCase):

    def test_do_sum(self):
        self.assertEqual(r.do_sum(3), 6)

    def test_do_factorial(self):
        self.assertEqual(r.do_factorial(3), 9)
