#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    # initialize new list to store result of div
    new_list = []
    # loop to iterate over the range of list_length
    for i in range(list_length):
        # a try-except-finally block to handle possible errors
        try:
            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)
        except ZeroDivisionError:
            # handle case when second element is 0
            print("division by 0")
            new_list.append(0)
        except TypeError:
            # handle case when an element is not an integer or float
            print("wrong type")
            new_list.append(0)
        except IndexError:
            # handle when list too short
            print("out of range")
            new_list.append(0)
        finally:
            pass
    return new_list
