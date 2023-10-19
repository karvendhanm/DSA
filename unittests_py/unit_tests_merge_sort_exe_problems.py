import unittest

from merge_sort_py import min_gap, num_distinct_integers, deduplicate_array, find_modes, compute_median


class TestProgramMergeSortExeProblem(unittest.TestCase):
    def test_case2_1(self):
        self.assertEqual(min_gap([-9, -11, 14, 9, 0, 3, 9]), 0)

    def test_case_2(self):
        self.assertEqual(min_gap([]), None)

    def test_case_2(self):
        self.assertEqual(min_gap([0]), None)

    def test_case_3(self):
        self.assertEqual(num_distinct_integers([]), 0)

    def test_case_4(self):
        self.assertEqual(num_distinct_integers([0]), 1)

    def test_case_5(self):
        self.assertEqual(deduplicate_array([]), [])

    def test_case_6(self):
        self.assertEqual(deduplicate_array([-6]), [-6])

    def test_case_7(self):
        self.assertEqual(deduplicate_array([-6, -6, -6, 6, 6, -6, -5]), [-6, -5, 6])

    def test_case_8(self):
        self.assertEqual(find_modes([1, 1, 3, 2, 4, 4, 5, 5, 6]), [1, 4, 5])

    def test_case_9(self):
        self.assertEqual(find_modes([]), [])

    def test_case_10(self):
        self.assertEqual(find_modes([5]), [5])

    def test_case_11(self):
        self.assertEqual(find_modes([1, 1, 3, 2, 4, 4, 4, 5, 5, 6]), [4])

    def test_case_12(self):
        self.assertEqual(find_modes([1, 1, 3, 2, 4, 4, 4, 5, 5, 5, 6]), [4, 5])

    def test_case_13(self):
        self.assertEqual(find_modes([-1, -1, -1, -2, -2, -2, -3, -3, -3]), [-3, -2, -1])

    def test_case_14(self):
        self.assertEqual(compute_median([]), [])

    def test_case_15(self):
        self.assertEqual(compute_median([5]), [5])

    def test_case_16(self):
        self.assertEqual(compute_median([1, 2, 3, 4, 5, 6, 7]), 4)

