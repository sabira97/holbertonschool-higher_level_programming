#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    length = len(roman_string)

    for i in range(length):
        current_value = roman_map[roman_string[i]]

        # If this value is less than the next value, subtract it
        if i + 1 < length and current_value < roman_map[roman_string[i + 1]]:
            total -= current_value
        else:
            total += current_value

    return total
