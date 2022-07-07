import pytest

from CodeWars.sum_groups import sum_groups


def test_sum_groups():
    assert sum_groups([2, 1, 2, 2, 6, 5, 0, 2, 0, 5, 5, 7, 7, 4, 3, 3, 9]) == 8


if __name__ == '__main__':
    pytest.main()
