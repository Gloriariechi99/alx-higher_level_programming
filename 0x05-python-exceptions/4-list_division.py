#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n = 0
    res = 0
    new_list = []
    for n in range(0, list_length):
        try:
            res = (my_list_1[n] / my_list_2[n])
        except TypeError:
            res = 0
            print("wrong type")
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            new_list.append(res)
    return new_list
