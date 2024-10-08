"""
ValidateVoters.py

This program prompts the user to enter their age and checks if they are eligible to vote.

Example usage:

    $ python ValidateVoters.py
    Enter voter's age: 25
    Voter of 25 years is eligible to vote.
    Thank you for voting

"""

import math

def validate_voter():
    """
    Prompts the user to enter their age and checks if they are eligible to vote.

    Returns:
        None
    """
    age = eval(input("Enter voter's age:"))
    # Checking eligibility
    if age >= 18:
        print("Voter of", age, "years is eligible to vote.")
        print("Thank you for voting")

if __name__ == "__main__":
    validate_voter()