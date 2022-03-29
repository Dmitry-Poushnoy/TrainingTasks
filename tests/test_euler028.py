import pytest as pytest

from EulerProblems.euler028.euler028 import sum_diagonal, sum_of_4steps


def test_sum_diagonal():
    assert sum_diagonal(5) == 101
    assert sum_diagonal(7) == 261
    assert sum_diagonal(9) == 537


def test_sum_of_4steps():
    assert sum_of_4steps(3, 2) == 24
    assert sum_of_4steps(13, 4) == 76
    assert sum_of_4steps(31, 6) == 160


if __name__ == '__main__':
    pytest.main()
