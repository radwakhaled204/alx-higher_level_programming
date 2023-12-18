#!/usr/bin/python3
"""append_write"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    and returns the number of characters added.

    Args:
        filename (str): The name of the file to append. Defaults to "".
        text (str): The string to append. Defaults to "".

    Returns:
        int: The number of characters added.

    Raises:
        PermissionError: If the file cannot be accessed.
    """
    # Use the with statement to open the file in append mode
    with open(filename, "a", encoding="utf-8") as f:
        # Write the text to the file and return the number of characters added
        return f.write(text)
