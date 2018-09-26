import unittest

import src.search_simple as simple


class TestSearchSimple(unittest.TestCase):

	def test_sanity(self):
		self.assertEqual(True, True)

	def test_something(self):
		self.assertEqual('something', simple.something())
