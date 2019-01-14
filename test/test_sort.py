import unittest

import src.sort as sort


class TestSort(unittest.TestCase):

    def test_selection_sort(self):
        artists_unsorted = {'blue nile': 47, 'prince': 14, 'ethereal': 50}
        artists_sorted = {'ethereal': 50, 'blue nile': 47, 'prince': 14}
        self.assertEqual(artists_sorted, sort.selection_sort(artists_unsorted))
