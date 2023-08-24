#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        count = 0
        for item in row:
            count = count + 1
            print('{:d}'.format(item), end=(" " if count < len(row) else ""))
        print()
