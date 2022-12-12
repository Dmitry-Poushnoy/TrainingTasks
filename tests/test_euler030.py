import pytest

from EulerProblems.euler030.euler030 import is_power_number, sum_power_numbers


def test_is_power_number():
    assert is_power_number(1634, 4) is True
    assert is_power_number(8208, 4) is True
    assert is_power_number(9474, 4) is True
    assert is_power_number(1, 4) is False


def test_sum_power_numbers():
    assert sum_power_numbers(4) == 19316


if __name__ == '__main__':
    pytest.main()
