#!/usr/bin/python3
"""function that writes a string to a text file"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to "".

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the file cannot be accessed.
    """
    # Use the with statement to open the file
    with open(filename, encoding="utf-8") as f:
        # Read the file content and print it to stdout
        print(f.read(), end="")
