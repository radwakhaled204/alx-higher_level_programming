#!/usr/bin/python3
"""module text_indentation, Adds two new lines after a set of characters."""


def text_indentation(text):
    """Prints text with added two newlines after
    each of these characters {'.', '?', ':'}."""

    # Check if the input is a string, otherwise raise an error
    if type(text) is not str:
        raise TypeError("text must be a string")

    # Loop through the special characters that trigger a new line
    for delim in ".:?":
        # Split the text by the current delimiter
        # and remove any spaces after it
        # Then join the text segments with the delimiter and two new lines
        text = (delim + "\n\n").join(
                [line.strip(" ") for line in text.split(delim)])

    # Print the formatted text without an extra new line at the end
    print("{}".format(text), end="")
