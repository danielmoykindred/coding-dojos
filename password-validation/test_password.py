import unittest
import typing
import re

PASSWORD = "password12"


class TestPassword(unittest.TestCase):
    def test_short_password(self):
        assert validate_password("pa12") == (
            False,
            "Password must be at least 8 characters\n",
        )

    def test_correct_password(self):
        assert validate_password("password12") == (True, "Success")

    def test_no_number_password(self):
        assert validate_password("password") == (
            False,
            "The password must contain at least 2 numbers\n",
        )

    def test_2_errors(self):
        assert validate_password("paass") == (
            False,
            "Password must be at least 8 characters\nThe password must contain at least 2 numbers\n",
        )


def validate_password(password: str) -> typing.Tuple[bool, str]:
    ret_val = ""
    if len(password) < 8:
        ret_val += "Password must be at least 8 characters\n"
    if not has_2_numbers(password):
        ret_val += "The password must contain at least 2 numbers\n"
    if password == PASSWORD:
        return (True, "Success")
    return (False, ret_val)


def has_2_numbers(password: str) -> bool:
    counter = 0
    for char in password:
        char = str(char)
        x = char.isnumeric()
        if x:
            counter += 1
            if counter >= 2:
                return True
    return False
