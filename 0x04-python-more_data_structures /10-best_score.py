#!/usr/bin/python3

def best_score(a_dictionary):
    # check if the dictionary is empty or None to return none
    if not a_dictionary:
        return None

    # create variable to store the best key and score
    best_key = None
    best_score = 0
    # loop through key/value pair in the dictionary
    for key, value in a_dictionary.items():
        # check if value is greater than the best score
        if value > best_score:
            best_key = key
            best_score = value
    return best_key
