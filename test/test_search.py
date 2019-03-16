import unittest

import src.search as search


class TestSearch(unittest.TestCase):

    def test_simple(self):
        self.assertGreaterEqual(100, search.simple())

    def test_binary_happy(self):
        query = 42
        list_happy = [2, 13, 24, 35, 42, 57, 68, 79]
        self.assertEqual('found 42', search.binary(query, list_happy))

    def test_binary_unhappy(self):
        query = 42
        list_unhappy = [2, 13, 24, 35, 46, 57, 68, 79]
        self.assertEqual('could not find 42', search.binary(query, list_unhappy))
