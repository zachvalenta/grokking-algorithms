import unittest

import src.sort as sort


class TestSort(unittest.TestCase):

    def test_selection_sort(self):
        self.assertEqual([50, 47, 14], sort.selection_sort([47, 14, 50]))
