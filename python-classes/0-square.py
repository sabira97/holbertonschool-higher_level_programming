#!/usr/bin/python3
"""Module that defines a Square class with validation."""

class Square:
    """A class that defines a square with size validation."""

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): Size of the square. Must be >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
