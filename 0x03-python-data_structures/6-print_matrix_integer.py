#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_str = ""
        for number in row:
            row_str = row_str + "{} ".format(number)
        print(row_str[:-1])
