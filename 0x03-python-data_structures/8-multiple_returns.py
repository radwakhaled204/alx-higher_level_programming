#!/usr/bin/python3

def multiple_returns(sentence):
    # check if the sentence is empty to return none
    if not sentence:
        return (0, None)
    else:
        # return a tuple with length of the sentence and its first character
        return (len(sentence), sentence[0])
