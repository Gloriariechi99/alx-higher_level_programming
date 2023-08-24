#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    big_int = 0
    for item in my_list:
        if item > big_int:
            big_int = item
    return big_int
