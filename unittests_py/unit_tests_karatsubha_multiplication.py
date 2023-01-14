import unittest

from karatsubha_multiplication_py import karatsubha_multiplication as km

class TestKaratSubha(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(km(5, 6), 30)

    def test_case_2(self):
        self.assertEqual(km(0, 456), 0)

    def test_case_3(self):
        self.assertEqual(km(1, 12), 12)

    def test_case_4(self):
        self.assertEqual(
            km(3141592653589793238462643383279502884197169399375105820974944592,
               2718281828459045235360287471352662497757247093699959574966967627)
             , 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184)

    def test_case_5(self):
        self.assertEqual(km(12, 1), 12)

    def test_case_6(self):
        self.assertEqual(km(1, 0), 0)