import unittest

from merge_sort_py import min_gap, num_distinct_integers, deduplicate_array, find_modes, compute_median
from merge_sort_py import find_2nd_biggest_number_v1, find_2nd_biggest_number_v2


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

    def test_case_17(self):
        self.assertEqual(find_2nd_biggest_number_v1([5, 7, 3, 0, 2, 4, 9, 1]), 7)

    def test_case_18(self):
        self.assertEqual(find_2nd_biggest_number_v1([]), None)

    def test_case_19(self):
        self.assertEqual(find_2nd_biggest_number_v1([-1]), None)

    def test_case_20(self):
        self.assertEqual(find_2nd_biggest_number_v1([3, 17]), 3)

    def test_case_21(self):
        self.assertEqual(find_2nd_biggest_number_v1([4, 9, 10]), 9)

    def test_case_22(self):
        self.assertEqual(find_2nd_biggest_number_v1([-9, -424, 9, 15]), 9)

    def test_case_23(self):
        self.assertEqual(find_2nd_biggest_number_v1([-9, -424, -3, 15]), -3)

    def test_case_24(self):
        self.assertEqual(find_2nd_biggest_number_v1([5, 7, 3, 0, 2, 4, 9, 1]), 7)

    def test_case_25(self):
        self.assertEqual(find_2nd_biggest_number_v2([]), None)

    def test_case_26(self):
        self.assertEqual(find_2nd_biggest_number_v2([-1]), None)

    def test_case_27(self):
        self.assertEqual(find_2nd_biggest_number_v2([3, 17]), 3)

    def test_case_28(self):
        self.assertEqual(find_2nd_biggest_number_v2([4, 9, 10]), 9)

    def test_case_29(self):
        self.assertEqual(find_2nd_biggest_number_v2([-9, -424, 9, 15]), 9)

    def test_case_30(self):
        self.assertEqual(find_2nd_biggest_number_v2([-9, -424, -3, 15]), -3)

























