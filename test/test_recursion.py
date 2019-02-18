import unittest

import src.recursion as r


class TestRecursion(unittest.TestCase):

    # TODO: parameterize https://stackoverflow.com/a/34094/6813490
    def test_countdown(self):
        self.assertEqual(None, r.countdown(0))

    def test_do_sum(self):
        self.assertEqual(10, r.do_sum(4))

    def test_do_factorial(self):
        self.assertEqual(24, r.do_factorial(4))
