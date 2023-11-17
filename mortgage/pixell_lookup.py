"""
Description: Enumerations to keep track of valid mortgage rates 
and payment frequencies. A list to keep track of valid amortization periods.
Author: ACE Department
Edited By: Harshdeep Singh Virk 
Date: 08/11/2023
Usage: The enumerations and list in this file may be used when working 
with mortgages to ensure only valid rates, Frequencies and Amortization 
periods are used.
"""


from enum import Enum

class MortgageRate(Enum):
    """MortgageRate as an enumeration """
    FIXED_5 = 0.0500
    FIXED_3 = 0.0579
    FIXED_1 = 0.0589
    VARIABLE_5 = 0.0650
    VARIABLE_3 = 0.0660
    VARIABLE_1 = 0.0679

class MortgageFrequency(Enum):
    """MortgageFrequency as an enumeration"""
    MONTHLY = 12
    BI_WEEKLY = 26
    WEEKLY = 52

VALID_AMORTIZATION = [5, 10, 15, 20, 25, 30]
