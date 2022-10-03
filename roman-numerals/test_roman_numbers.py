import unittest

NUMERALS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


class TestRomanNumeralClass(unittest.TestCase):
    def test_no_3_numbers_repeat(self):
        pass

    def test_vld_not_repeated(self):
        pass

    def test_ixc_substracting(self):
        pass

    def test_no_0_is_added(self):
        pass

    def validate_sum_is_correct(self, roman_numeral: str, expected_target: int):
        assert self._process_number(roman_numeral) == expected_target

    def _process_number(self, roman_numeral, last_digit=0, sum=0):

        number = list(roman_numeral)
        while number:
            current_digit = NUMERALS[number.pop()]
            if last_digit > current_digit:
                sum -= current_digit
            else:
                sum += current_digit
            last_digit = current_digit
        return sum


def run_tests():
    testing = TestRomanNumeralClass()
    testing.validate_sum_is_correct("MLCVII", 1057)


if __name__ == "__main__":
    run_tests()
