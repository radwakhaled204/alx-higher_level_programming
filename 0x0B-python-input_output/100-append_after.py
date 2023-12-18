#!/usr/bin/python3
"""inserts a text to a file, after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename (str): The name of the file to modify
        search_string (str): The string to search for
        new_string (str): The string to insert
    """
    # Use the with statement to open the file in read mode
    with open(filename, "r", encoding="utf-8") as f:
        # Read the file content as a list of lines
        lines = f.readlines()

    # Use the with statement to open the file in write mode
    with open(filename, "w", encoding="utf-8") as f:
        # Loop through the lines
        for line in lines:
            # Write the current line to the file
            f.write(line)
            # If the current line contains the search string,
            # write the new string to the file
            if search_string in line:
                f.write(new_string)
