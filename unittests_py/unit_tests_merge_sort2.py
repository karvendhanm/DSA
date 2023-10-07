import unittest

from merge_sort_py import combine_two_arrays, merge_sort2


class TestProgramMergeSort2(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(combine_two_arrays([], [2, 3]), [2, 3])

    def test_case_2(self):
        self.assertEqual(combine_two_arrays([2, 3], []), [2, 3])

    def test_case_3(self):
        self.assertEqual(combine_two_arrays([2, 3, 5], [1, 4, 7]), [1, 2, 3, 4, 5, 7])

    def test_case_4(self):
        self.assertEqual(combine_two_arrays([2, 3], [2, 2, 4]), [2, 2, 2, 3, 4])

    def test_case_5(self):
        self.assertEqual(combine_two_arrays([], []), [])

    def test_case_6(self):
        self.assertEqual(combine_two_arrays([-1, -1, -1], []), [-1, -1, -1])

    def test_case_7(self):
        self.assertEqual(combine_two_arrays([], [-1, -1, -1]), [-1, -1, -1])

    def test_case_8(self):
        self.assertEqual(combine_two_arrays([-6], [-4, -3, -2, -1]), [-6, -4, -3, -2, -1])

    def test_case_9(self):
        self.assertEqual(merge_sort2([5, 4, 1, 8, 7, 2, 6, 3]), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_case_10(self):
        self.assertEqual(merge_sort2([0, -3, 7, 8]), [-3, 0, 7, 8])

    def test_case_11(self):
        self.assertEqual(merge_sort2([]), [])

    def test_case_12(self):
        self.assertEqual(merge_sort2([3, 2, 1]), [1, 2, 3])
