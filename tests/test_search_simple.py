import unittest

import src.search_simple as simple


class TestSearch(unittest.TestCase):

	def test_simple(self):
		self.assertGreaterEqual(100, simple.simple_search())

	def test_binary(self):
		pass
