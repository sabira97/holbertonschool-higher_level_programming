#!/usr/bin/python3
"""Private size atributu ilə kvadrat sinfi"""

class Square:
    """Ölçüsü (`size`) gizli (`private`) olan kvadrat sinfi."""
    def __init__(self, size):
        """İlkinizasiya zamanı `size` atributunu `__size` olaraq saxlayır."""
        self.__size = size

