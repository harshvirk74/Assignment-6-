"""
Description: A class meant to manage Mortgage options.
Author: Harshdeep Singh Virk 
Date: 08/11/2023
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""
from pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION

class Mortgage:
    def __init__(self, loan_amount, rate, frequency, amortization):
        if loan_amount <= 0:
            raise ValueError("Loan Amount must be positive")
        if not isinstance(rate, MortgageRate):
            raise ValueError("Rate must be a MortgageRate enum value")
        if not isinstance(frequency, MortgageFrequency):
            raise ValueError("Frequency must be a MortgageFrequency enum value")
        if amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization period not valid")

        self.loan_amount = loan_amount
        self.rate = rate
        self.frequency = frequency
        self.amortization = amortization

    @property
    def loan_amount(self):
        return self._loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        if value <= 0:
            raise ValueError("Loan Amount must be positive")
        self._loan_amount = value

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        if not isinstance(value, MortgageRate):
            raise ValueError("Rate must be a MortgageRate enum value")
        self._rate = value

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, value):
        if not isinstance(value, MortgageFrequency):
            raise ValueError("Frequency must be a MortgageFrequency enum value")
        self._frequency = value

    @property
    def amortization(self):
        return self._amortization

    @amortization.setter
    def amortization(self, value):
        if value not in VALID_AMORTIZATION:
            raise ValueError("Amortization period not valid")
        self._amortization = value

    def calculate_payment(self):
        rate_per_period = self.rate.value / self.frequency.value
        total_payments = self.amortization * self.frequency.value
        payment = self.loan_amount * (rate_per_period * (1 + rate_per_period) ** total_payments) / ((1 + rate_per_period) ** total_payments - 1)
        return round(payment, 2)

    def __str__(self):
        payment = self.calculate_payment()
        return f"Mortgage Amount: ${self.loan_amount:,.2f}\n" \
               f"Rate: {self.rate.value:.2%}\n" \
               f"Amortization: {self.amortization} years\n" \
               f"Frequency: {self.frequency.name.replace('_', ' ').title()}\n" \
               f"Calculated Payment: ${payment:,.2f}"

    def __repr__(self):
        return (f"Mortgage(loan_amount={self.loan_amount}, rate={self.rate}, "
                f"frequency={self.frequency}, amortization={self.amortization})")
