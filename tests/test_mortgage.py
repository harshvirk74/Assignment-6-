"""
Description: A class used to test the Mortgage class.
Author: Harshdeep Singh Virk 
Date: 8/11/2023
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""

from unittest import TestCase
from mortgage import Mortgage
from pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION

class MortgageTests(TestCase):

    def test_negative_loan_amount_raises_value_error(self):
        with self.assertRaises(ValueError):
            Mortgage(-1000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 25)

    def test_zero_loan_amount_raises_value_error(self):
        with self.assertRaises(ValueError):
            Mortgage(0, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 25)

    def test_invalid_mortgage_rate_raises_value_error(self):
        with self.assertRaises(ValueError):
            Mortgage(200000, 'FIXED_5', MortgageFrequency.MONTHLY, 25)

    def test_invalid_mortgage_frequency_raises_value_error(self):
        with self.assertRaises(ValueError):
            Mortgage(200000, MortgageRate.FIXED_5, 'MONTHLY', 25)

    def test_invalid_amortization_raises_value_error(self):
        with self.assertRaises(ValueError):
            Mortgage(200000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 35)

    def test_valid_mortgage_initialization(self):
        mortgage = Mortgage(200000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 25)
        self.assertIsInstance(mortgage, Mortgage)

    def test_payment_calculation_with_fixed_rate(self):
        mortgage = Mortgage(200000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 25)
        # Use the formula to calculate the expected payment and round to two decimal places
        expected_payment = round(mortgage.calculate_payment(), 2)
        self.assertAlmostEqual(mortgage.calculate_payment(), expected_payment)

    def test_payment_calculation_changes_with_rate(self):
        mortgage = Mortgage(200000, MortgageRate.FIXED_3, MortgageFrequency.MONTHLY, 25)
        expected_payment = round(mortgage.calculate_payment(), 2)
        self.assertNotEqual(mortgage.calculate_payment(), Mortgage(200000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 25).calculate_payment())

    def test_payment_calculation_changes_with_frequency(self):
        mortgage = Mortgage(200000, MortgageRate.FIXED_5, MortgageFrequency.BI_WEEKLY, 25)
        expected_payment = round(mortgage.calculate_payment(), 2)
        self.assertNotEqual(mortgage.calculate_payment(), Mortgage(200000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 25).calculate_payment())

    def test_payment_calculation_changes_with_amortization(self):
        mortgage = Mortgage(200000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 20)
        expected_payment = round(mortgage.calculate_payment(), 2)
        self.assertNotEqual(mortgage.calculate_payment(), Mortgage(200000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 25).calculate_payment())

    def test_loan_amount_setter(self):
        mortgage = Mortgage(200000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 25)
        mortgage.loan_amount = 300000
        self.assertEqual(mortgage.loan_amount, 300000)

    def test_rate_setter(self):
        mortgage = Mortgage(200000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 25)
        mortgage.rate = MortgageRate.FIXED_3
        self.assertEqual(mortgage.rate, MortgageRate.FIXED_3)

    def test_frequency_setter(self):
        mortgage = Mortgage(200000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 25)
        mortgage.frequency = MortgageFrequency.WEEKLY
        self.assertEqual(mortgage.frequency, MortgageFrequency.WEEKLY)

    def test_amortization_setter(self):
        mortgage = Mortgage(200000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 25)
        mortgage.amortization = 20
        self.assertEqual(mortgage.amortization, 20)

    def test_string_representation(self):
        mortgage = Mortgage(200000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 25)
        expected_str = f"Mortgage Amount: $200000.00\nRate: 5.00%\nAmortization: 25\nFrequency: Monthly -- Calculated Payment: ${mortgage.calculate_payment():.2f}"
        self.assertEqual(str(mortgage), expected_str)

    def test_repr_representation(self):
        mortgage = Mortgage(200000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 25)
        expected_repr = "Mortgage(loan_amount=200000, rate=MortgageRate.FIXED_5, frequency=MortgageFrequency.MONTHLY, amortization=25)"
        self.assertEqual(repr(mortgage), expected_repr)

    # Additional tests if needed

if __name__ == "__main__":
    TestCase.main()
