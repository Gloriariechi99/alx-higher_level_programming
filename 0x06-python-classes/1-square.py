#!/usr/bin/python3
"""
tells the operating system which intepreter
should be used to execute the file
"""


class Square:
    """
    class that defines a square based on
    the size attribute
    """

    def __init__(self, size):
        """
        initializes a square with the given size


        parameters:
            size (int): represents the size of each side of the square
        """

        self.__size = size
