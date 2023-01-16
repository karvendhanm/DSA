import unittest

from number_of_inversions_py import count_num_inversions

class TestNumberOfInversions(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(count_num_inversions([1, 3, 5, 2, 4, 6]), 3)

    def test_case_2(self):
        self.assertEqual(count_num_inversions([4, 3, 6, 5, 1, 2]), 10)

    def test_case_3(self):
        self.assertEqual(count_num_inversions([6, 5, 4, 3, 2, 1]), 15)

    def test_case_4(self):
        self.assertEqual(count_num_inversions([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 45)
