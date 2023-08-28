#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elem = 0
    item = 0
    for elem in range(0, x):
        try:
            print("{:d}".format(my_list[elem]), end="")
            item = item + 1
        except (ValueError, TypeError):
            continue

    print()
    return item
