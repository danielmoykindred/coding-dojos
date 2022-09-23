import unittest
import typing

NUMERAL_CONVERSIONS = {"I": 1, "V": 5, "X": 10, "L": 50}


class TestRomanNumerals(unittest.TestCase):
    def test_convert_1(self):
        assert convert_roman_numerals("I") == 1

    def test_convert_2(self):
        assert convert_roman_numerals("II") == 2

    def test_convert_4(self):
        assert convert_roman_numerals("IV") == 4

    def test_convert_5(self):
        assert convert_roman_numerals("V") == 5

    def test_convert_6(self):
        assert convert_roman_numerals("VI") == 6

    def test_convert_10(self):
        assert convert_roman_numerals("X") == 10

    def test_convert_11(self):
        assert convert_roman_numerals("XI") == 11

    def test_lt_pair(self):
        assert check_number_pair(("I", "V")) is True

    def test_gt_pair(self):
        assert check_number_pair(("V", "I")) is False

    def test_eq_pair(self):
        assert check_number_pair(("I", "I")) is True

    def test_convert_40(self):
        assert convert_roman_numerals("XL") == 40

    def test_convert_47(self):
        assert convert_roman_numerals("XLVII") == 47


def check_number_pair(pair: tuple):
    value1, value2 = pair
    if NUMERAL_CONVERSIONS[value1] <= NUMERAL_CONVERSIONS[value2]:
        return True
    return False


def subtract_numbers(numeral: str):
    return NUMERAL_CONVERSIONS[numeral[1]] - NUMERAL_CONVERSIONS[numeral[0]]


def convert_roman_numerals(numeral: str) -> int:
    sum_of_nums = 0
    if len(numeral) == 1:
        return NUMERAL_CONVERSIONS[numeral]
    for index, char in enumerate(numeral):
        if index + 1 == len(numeral):
            previous_char = numeral[index - 1]
            if NUMERAL_CONVERSIONS[previous_char] >= NUMERAL_CONVERSIONS[char]:
                sum_of_nums += NUMERAL_CONVERSIONS[char]
            return sum_of_nums
        next_char = numeral[index + 1]
        if NUMERAL_CONVERSIONS[char] < NUMERAL_CONVERSIONS[next_char]:
            sum_of_nums += subtract_numbers(str(char + next_char))
        else:
            sum_of_nums += NUMERAL_CONVERSIONS[char]

    return sum_of_nums


# X L V  I I _
# _ X L  V I I
# _ T F  T T T
# _ sum1 sum2

# _ X L I V
# _ T F T F
# _ sum1 sum2
