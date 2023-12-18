#!/usr/bin/python3
"""script to writes a string to a text file"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and
    returns the number of characters written.

    Args:
        filename (str): The name of the file to write. Defaults to "".
        text (str): The string to write. Defaults to "".

    Returns:
        int: The number of characters written.

    Raises:
        PermissionError: If the file cannot be accessed.
    """
    # Use the with statement to open the file in write mode
    with open(filename, "w", encoding="utf-8") as f:
        # Write the text to the file and return
        # the number of characters written
        return f.write(text)
