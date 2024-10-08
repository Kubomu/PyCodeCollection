"""
Determines whether a given year is a leap year or not.

A year is a leap year if it is divisible by 4 but not by 100 or if it is divisible by 400.

Parameters:
    year (int): The year to check

Returns:
    bool: True if the year is a leap year, False otherwise

Example:
    >>> DeterminingLeapYear(2020)
    The year 2020 is a leap year: True
"""

def DeterminingLeapYear(year):
    """
    See module docstring for details.
    """
    # A leap year is divisible by 4
    isLeapYear = (year % 4 == 0)

    # A leap year is divisible by 4 but not by 100
    isLeapYear = isLeapYear and (year % 100!= 0)

    # A leap year is divisible by 4 but not by 100 or divisible by 400
    isLeapYear = isLeapYear or (year % 400 == 0)

    print(f"The year {year} is a leap year: {isLeapYear}")

year = eval(input("Enter a year: "))
DeterminingLeapYear(year)