import pytest

from EulerProblems.euler033.euler033 import possible_numerators, get_common_digit, get_1digit_list


def test_possible_numerators():
    assert possible_numerators(100)[10] == 24
    assert possible_numerators(100)[-1] == 98


def test_get_common_digit():
    assert get_common_digit(12, 34) == []
    assert get_common_digit(37, 23) == [3]
    assert get_common_digit(37, 73) == [3, 7]
    assert get_common_digit(73, 37) == [7, 3]


def test_get_1digit_list():
    assert get_1digit_list(13, 39, 3) == [1, 9]
    assert get_1digit_list(39, 13, 3) == [0, 1]
    assert get_1digit_list(13, 39, 5) == [13, 39]
    assert get_1digit_list(13, 21, 1) == [0, 1]


if __name__ == '__main__':
    pytest.main()
