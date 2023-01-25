import unittest

from number_of_inversions_py import count_num_inversions, CountSplitInversions, CountNumOfInversions

class TestNumberOfInversions(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(count_num_inversions([1, 3, 5, 2, 4, 6]), 3)

    def test_case_2(self):
        self.assertEqual(count_num_inversions([4, 3, 6, 5, 1, 2]), 10)

    def test_case_3(self):
        self.assertEqual(count_num_inversions([6, 5, 4, 3, 2, 1]), 15)

    def test_case_4(self):
        self.assertEqual(count_num_inversions([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 45)

    def test_case_5(self):
        # when all the elements in the left array are smaller than all the
        # elements in the right array, then the number of split inversions
        # is zero.
        self.assertEqual(CountSplitInversions([1, 2, 3], [4, 5, 6]), ([1, 2, 3, 4, 5, 6], 0))

    def test_case_6(self):
        self.assertEqual(CountSplitInversions([4, 5, 6], [1, 2, 3]), ([1, 2, 3, 4, 5, 6], 9))

    def test_case_7(self):
        self.assertEqual(CountSplitInversions([7, 8], [1, 5, 6, 9, 13]), ([1, 5, 6, 7, 8, 9, 13], 6))

    def test_case_8(self):
        self.assertEqual(CountSplitInversions([], []), ([], 0))

    def test_case_9(self):
        self.assertEqual(CountSplitInversions([1, 5, 6, 9, 13], [7, 8]), ([1, 5, 6, 7, 8, 9, 13], 4))

    def test_case_10(self):
        self.assertEqual(CountNumOfInversions([5, 4, 6, 3, 2, 1]), ([1, 2, 3, 4, 5, 6], 13))

    def test_case_11(self):
        self.assertEqual(CountNumOfInversions([6, 5, 4, 3, 2, 1]), ([1, 2, 3, 4, 5, 6], 15))

    def test_case_12(self):
        self.assertEqual(CountNumOfInversions([]), ([], 0))

    def test_case_13(self):
        self.assertEqual(CountNumOfInversions([4, 2, 3, 1]), ([1, 2, 3, 4], 5))

    def test_case_14(self):
        self.assertEqual(CountNumOfInversions([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 45))




