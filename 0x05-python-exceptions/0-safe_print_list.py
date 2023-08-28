#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    item = 0
    elem_to_print = 0
    for item in range(0, x):
        try:
            print("{}".format(my_list[item]), end="")
            elem_to_print = elem_to_print + 1
        except IndexError:
            continue
    print()
    return elem_to_print
