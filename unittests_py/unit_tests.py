import unittest

from binary_search_py import binary_search

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(binary_search([36, 56, 66, 72, 76, 108], 76), 4)

    def test_case_2(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 6, 7, 8], 6), 4)

    def test_case_3(self):
        self.assertNotEqual(binary_search([1, 2, 3, 4, 6, 7, 8], 4), -1)

    def test_case_4(self):
        self.assertEqual(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)

    def test_case_5(self):
        self.assertEqual(binary_search([1, 5, 23, 111], 111), 3)

    def test_case_6(self):
        self.assertEqual(binary_search([1, 5, 23, 111], 5), 1)

    def test_case_7(self):
        self.assertEqual(binary_search([1, 5, 23, 111], 35), -1)

    def test_case_8(self):
        self.assertEqual(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 0), 0)

    def test_case_9(self):
        self.assertEqual(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 1), 1)

    def test_case_10(self):
        self.assertEqual(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 21), 2)

    def test_case_11(self):
        self.assertEqual(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 45), 4)

    def test_case_12(self):
        self.assertEqual(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 61), 6)

    def test_case_13(self):
        self.assertEqual(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 71), 7)

    def test_case_14(self):
        self.assertEqual(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 72), 8)

    def test_case_15(self):
        self.assertEqual(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 73), 9)

    def test_case_16(self):
        self.assertEqual(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 70), -1)

    def test_case_17(self):
        self.assertEqual(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], 355), 10)

    def test_case_18(self):
        self.assertEqual(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], 354), -1)

    def test_case_19(self):
        self.assertEqual(binary_search([1, 5, 23, 111], 120), -1)

    def test_case_20(self):
        self.assertEqual(binary_search([5, 23, 111], 3), -1)





