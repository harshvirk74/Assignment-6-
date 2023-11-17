"""
Description: A client program written to verify accuracy of and 
calculate payments for PiXELL River Mortgages.
Author: ACE Faculty
Edited/ by: Harshdeep Singh Virk 
Date: 08/11/2023
"""
# Import necessary modules from the mortgage package
from mortgage import Mortgage
from pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION

# Main batch processing function
def main():
    try:
        # Open the file and process each line
        with open("data/pixell_river_mortgages.txt", "r") as input_file:
            print("**************************************************")
            
            for line in input_file:
                # Split the line into components
                amount_str, rate_str, amortization_str, frequency_str = line.strip().split(",")
                
                try:
                    # Convert string values to their respective types
                    amount = float(amount_str)
                    rate = MortgageRate[rate_str]
                    frequency = MortgageFrequency[frequency_str]
                    amortization = int(amortization_str)
                    
                    # Create a Mortgage instance
                    mortgage = Mortgage(amount, rate, frequency, amortization)
                    
                    # Print the mortgage details
                    print(mortgage)
                
                except ValueError as e:
                    # Catch explicit exceptions raised in the Mortgage class
                    print(f"Data: {line.strip()} caused Exception: {e}")
                
                except Exception as e:
                    # Catch any other exceptions
                    print(f"Data: {line.strip()} caused Exception: {e}")
                
                finally:
                    print("**************************************************")
    
    except FileNotFoundError as e:
        # Handle file not found error
        print(f"Error opening the mortgages file: {e}")

# Execute the batch processing function
if __name__ == "__main__":
    main()
