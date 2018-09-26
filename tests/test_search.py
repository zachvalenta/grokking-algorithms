import unittest

import src.search as search


class TestSearch(unittest.TestCase):

	def test_simple(self):
		self.assertGreaterEqual(100, search.simple())

	def test_binary(self):
		pass
