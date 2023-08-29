#!/usr/bin/python3
"""
tells the operating system which interpreter should
be used to execute the file
"""


class Square:
    """defines a class square"""

    def __init__(self, size=0):
        """initializes the square

        parameters:
            size (int): The size of the sides of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
