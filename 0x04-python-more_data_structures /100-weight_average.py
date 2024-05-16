#!/usr/bin/python3
def weight_average(my_list=[]):
    # check if list is empty and return 0 if yes
    if not my_list:
        return 0
    # create variables to store sum of weighted scores and weights
    weighted_sum = 0
    weight_sum = 0
    # loop through each tuple in the list
    for score, weight in my_list:
        # multiply score by weight and add it to weighted_sum
        weighted_sum += score * weight
        # add weight to weight_sum
        weight_sum += weight
    average = weighted_sum / weight_sum
    return average
