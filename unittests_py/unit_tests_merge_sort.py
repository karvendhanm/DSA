from merge_sort_py import merge_ascending, merge_sort
import unittest


class TestProgramMergeSort(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(merge_ascending([4, 4, 4, 5, 5], [2, 6]), [2, 4, 4, 4, 5, 5, 6])

    def test_case_2(self):
        self.assertEqual(merge_ascending([], []), [])

    def test_case_3(self):
        self.assertEqual(merge_ascending([2, 4, 5, 7], [1, 3, 6, 8]), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_case_4(self):
        self.assertEqual(merge_ascending([], [1, 3, 5, 7]), [1, 3, 5, 7])

    def test_case_5(self):
        self.assertEqual(merge_ascending([1, 3, 5, 7], []), [1, 3, 5, 7])

    def test_case_6(self):
        self.assertEqual(merge_ascending([1, 1, 2, 2, 3, 3, 3], [0.5, 1.5, 3.5, 4.5]),
                         [0.5, 1, 1, 1.5, 2, 2, 3, 3, 3, 3.5, 4.5])

    def test_case_7(self):
        self.assertEqual(merge_sort([3, 2, 7, 4, 5, 6, 1, 8]), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_case_8(self):
        self.assertEqual(merge_sort([]), [])

    def test_case_9(self):
        self.assertEqual(merge_sort([1, 3, 9, 5, 2]), [1, 2, 3, 5, 9])

    def test_case_10(self):
        self.assertEqual(merge_sort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])

    def test_case_11(self):
        self.assertEqual(merge_sort([1]), [1])
