import unittest

from merge_sort_py import min_gap, num_distinct_integers, deduplicate_array


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

