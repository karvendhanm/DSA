import unittest

from binary_search_py import binary_search

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(binary_search([36, 56, 66, 72, 76, 108], 76), 4)

    def test_case_2(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 6, 7, 8], 6), 4)

    def test_case_3(self):
        self.assertNotEqual(binary_search([1, 2, 3, 4, 6, 7, 8], 4), -1)


