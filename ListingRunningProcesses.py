"""
Lists all currently running processes on the system.

This script uses the `psutil` library to iterate over all running processes and
print their process ID and name.

Example:
    >>> python list_processes.py
    1234 chrome.exe
    5678 python.exe
    9012 explorer.exe
   ...
"""

# Importing the psutil library, which allows us to interact with processes on the system
import psutil

"""
Lists all currently running processes on the system.

Returns:
    None
"""
def list_processes():
    # Listing currently running processes
    for process in psutil.process_iter():
        # Printing the process ID and name of each running process
        print(process.pid, process.name())

# Call the function to list the processes
list_processes()