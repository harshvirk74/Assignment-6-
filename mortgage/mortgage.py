"""
Description: A class meant to manage Mortgage options.
Author: Harshdeep Singh Virk 
Date: 08/NOV/2023
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""

from mortgage.pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION

class Mortgage:
    """
    Class to represent a mortgage with specific details.
    """

    def __init__(self, amount, rate, amortization, frequency):
        """
        Initialize a Mortgage object with specified details.

        :param amount: The amount of the mortgage loan.
        :param rate: The annual interest rate (MortgageRate enum).
        :param amortization: The number of years to repay the mortgage loan.
        :param frequency: The number of payments per year (MortgageFrequency enum).
        """
        # Validate and set Loan Amount
        if amount > 0:
            self._amount = amount
        else:
            raise ValueError("Loan Amount must be positive.")

        # Validate and set Rate
        if isinstance(rate, MortgageRate):
            self._rate = rate
        else:
            raise ValueError("Invalid Rate provided.")

        # Validate and set Frequency
        if isinstance(frequency, MortgageFrequency):
            self._frequency = frequency
        else:
            raise ValueError("Invalid Frequency provided.")

        # Validate and set Amortization
        if amortization in VALID_AMORTIZATION:
            self._amortization = amortization
        else:
            raise ValueError("Invalid Amortization provided.")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value > 0:
            self._amount = value
        else:
            raise ValueError("Loan Amount must be positive.")

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        if isinstance(value, MortgageRate):
            self._rate = value
        else:
            raise ValueError("Invalid Rate provided.")

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, value):
        if isinstance(value, MortgageFrequency):
            self._frequency = value
        else:
            raise ValueError("Invalid Frequency provided.")

    @property
    def amortization(self):
        return self._amortization

    @amortization.setter
    def amortization(self, value):
        if value in VALID_AMORTIZATION:
            self._amortization = value
        else:
            raise ValueError("Invalid Amortization provided.")

    def calculate_payment(self):
        """
        Calculate the mortgage payment amount.

        :return: The calculated payment value.
        """
        n = self._amortization * self._frequency
        r = self._rate.value / self._frequency / 100
        p = self._amount
        payment = p * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
        return round(payment, 2)

    def __str__(self):
        """
        Return a string representation of the Mortgage object.

        :return: String representation of the Mortgage.
        """
        return (
            f"Mortgage Amount: ${self._amount:.2f}\n"
            f"Rate: {self._rate.name} ({self._rate.value:.4f})\n"
            f"Amortization: {self._amortization}\n"
            f"Frequency: {self._frequency.name} -- "
            f"Calculated Payment: ${self.calculate_payment():,.2f}"
        )

    def __repr__(self):
        """
        Return a raw representation of the Mortgage object.

        :return: Raw representation of the Mortgage.
        """
        return f"[{self._amount}, {self._rate.value:.4f}, {self._amortization}, {self._frequency.value}]"
