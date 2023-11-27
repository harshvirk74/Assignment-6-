"""
Description: A class used to test the Mortgage class.
Author: Harshdeep Singh Virk 
Date: 8/November/2023
Usage: Use the tests encapsulated within this class to test the Mortgage Payment class.
"""

import unittest
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION

class MortgageTests(unittest.TestCase):
    def test_invalid_loan_amount(self):
        with self.assertRaises(ValueError):
            Mortgage(-1000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)

    def test_invalid_rate(self):
        with self.assertRaises(ValueError):
            Mortgage(1000, "invalid_rate", MortgageFrequency.MONTHLY, 30)

    def test_invalid_frequency(self):
        with self.assertRaises(ValueError):
            Mortgage(1000, MortgageRate.FIXED_5, "invalid_frequency", 30)

    def test_invalid_amortization(self):
        with self.assertRaises(ValueError):
            Mortgage(1000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 35)

    def test_invalid_loan_amount(self):
        with self.assertRaises(ValueError):
            Mortgage(-1000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)

    def test_invalid_rate(self):
        with self.assertRaises(ValueError):
            Mortgage(1000, "invalid_rate", MortgageFrequency.MONTHLY, 30)

    def test_invalid_frequency(self):
        with self.assertRaises(ValueError):
            Mortgage(1000, MortgageRate.FIXED_5, "invalid_frequency", 30)

    def test_invalid_amortization(self):
        with self.assertRaises(ValueError):
            Mortgage(1000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 35)

    def test_valid_mortgage_initialization(self):
        mortgage = Mortgage(1000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
        self.assertIsInstance(mortgage, Mortgage)

    def test_loan_amount_accessor(self):
        mortgage = Mortgage(1000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
        self.assertEqual(mortgage.loan_amount, 1000)


    def test_invalid_loan_amount_mutator(self):
        mortgage = Mortgage(1000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
        with self.assertRaises(ValueError):
            mortgage.set_loan_amount(-1000)


    def test_calculate_payment_monthly(self):
        mortgage = Mortgage(1000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
        payment = mortgage.calculate_payment()
        self.assertIsInstance(payment, float)


    def test_str_method(self):
        mortgage = Mortgage(1000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
        mortgage_str = str(mortgage)
        self.assertIsInstance(mortgage_str, str)

    def test_repr_method(self):
        mortgage = Mortgage(1000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 30)
        mortgage_repr = repr(mortgage)
        self.assertIsInstance(mortgage_repr, str)

if __name__ == '_main_':
    unittest.main()
