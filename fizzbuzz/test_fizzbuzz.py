import unittest
import typing
import re

from fizzbuzz.fizzbuzzlist import BIG_LIST


class TestPassword(unittest.TestCase):
    def test_fizzbuzz_10(self):
        x, expected = test_fizzbuzz_n(10)
        assert x == expected

    def test_fizzbuzz_20(self):
        x, expected = test_fizzbuzz_n(20)
        assert x == expected

    def test_fizzbuzz_30(self):
        x, expected = test_fizzbuzz_n(30)
        assert x == expected


def test_fizzbuzz_n(n):
    x = []
    for i in range(1, n):
        x.append(transform_to_fizzbuzz(i))
    return x, BIG_LIST[0 : n - 1]


def transform_to_fizzbuzz(number):
    if divisable_by(number, 3) and divisable_by(number, 5):
        return "fizzbuzz"
    elif divisable_by(number, 3):
        return "fizz"
    elif divisable_by(number, 5):
        return "buzz"
    # if in_string(number, 3) and in_string(number, 5):
    #     return "fizzbuzz"
    # elif in_string(number, 3):
    #     return "fizz"
    # elif in_string(number, 5):
    #     return "buzz"
    else:
        return number


def divisable_by(number, param):
    return number % param == 0


def in_string(number, param):
    return str(param) in str(number)
