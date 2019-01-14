import unittest

import src.recursion as r


class TestRecursion(unittest.TestCase):

    # TODO: parameterize https://stackoverflow.com/a/34094/6813490
    def test_do_sum(self):
        self.assertEqual(r.do_sum(4), 10)

    def test_do_factorial(self):
        self.assertEqual(r.do_factorial(4), 24)
