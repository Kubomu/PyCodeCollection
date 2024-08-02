"""
Module for securely collecting username and password from user.

This module uses the `getpass` module to securely collect a password from the user
without echoing the input to the console.

Example:
    >>> from secure_input import collect_credentials
    >>> username, password = collect_credentials()
    Enter username: john_doe
    Enter password: 
    >>> print(username)
    john_doe
    >>> print(password)
    my_secret_password

Functions:
    collect_credentials: Collect username and password from user.
"""

from getpass import getpass

def collect_credentials():
    """
    Collect username and password from user.

    This function uses the built-in `input` function to collect the username and
    the `getpass` function from the `getpass` module to securely collect the password.

    Args:
        None

    Returns:
        tuple: (username, password)

    Example:
        >>> username, password = collect_credentials()
        Enter username: john_doe
        Enter password: 
        >>> print(username)
        john_doe
        >>> print(password)
        my_secret_password
    """
    username = input('Enter username: ')
    password = getpass('Enter password: ')
    return username, password

# Example usage:
if __name__ == '__main__':
    username, password = collect_credentials()
    print(f"Username: {username}")
    print(f"Password: {'*' * len(password)}")  # Don't print the actual password