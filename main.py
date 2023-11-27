"""
Description: A client program written to verify accuracy of and 
calculate payments for PiXELL River Mortgages.
Author: ACE Faculty
Edited/ by: Harshdeep Singh Virk 
Date: 08/11/2023
"""
### REQUIREMENT
### ADD IMPORT STATEMENTS FOR THE MORTGAGE CLASS, THE 
### MORTGAGERATE AND MORTGAGEFREQUENCY ENUMERATIONS AND THE 
### VALID_AMORTIZATION LIST

from mortgage.mortgage import Mortgage  # Import the Mortgage class
from mortgage.pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION

import logging

# Set up logging configuration
logging.basicConfig(filename='mortgage_log.txt', level=logging.INFO)

try:
    with open("data\\pixell_river_mortgages.txt", "r") as input:
        print("**************************************************")

        for data in input:
            items = data.split(",")

            try:
                amount = float(items[0])
                rate = items[1]
                amortization = int(items[2])
                frequency = int(items[3])  # Convert frequency to integer

                # Instantiate a Mortgage object
                mortgage = Mortgage(amount, MortgageRate[rate], amortization, MortgageFrequency(frequency))

                # Print the Mortgage object
                print(mortgage)

                # Log the successful creation of Mortgage objects
                logging.info(f"Successfully created Mortgage object: {mortgage}")

            except ValueError as e:
                # This except block will catch Explicit exceptions:
                # Those raised by the programmer in the Mortgage class.
                print(f"Data: {data.strip()} caused Exception: {e}")

                # Log the failed creation of Mortgage objects
                logging.warning(f"Failed to create Mortgage object: {data.strip()} - Exception: {e}")

            except Exception as e:
                # This except block will catch Implicit exceptions:
                # Those raised through normal execution.
                print(f"Data: {data.strip()} caused Exception: {e}")

                # Log the failed creation of Mortgage objects
                logging.warning(f"Failed to create Mortgage object: {data.strip()} - Exception: {e}")

            finally:
                print("**************************************************")

except FileNotFoundError as e:
    print(f"File not found: {e}")
    logging.error(f"File not found: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    logging.error(f"Unexpected error: {e}")
