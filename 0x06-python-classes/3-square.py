#!/usr/bin/python3
"""
tells the operating system which interpreter
executes the file
"""


class Square:
    """defines a class square"""

    def __init__(self, size=0):
        """
        initializes the square

        parameters:
            size (int): repersents the size of the side of the sqaure
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """public instance method that retuurns the current area"""
        return (self.__size ** 2)
