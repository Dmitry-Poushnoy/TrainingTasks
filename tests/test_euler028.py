import pytest as pytest

from EulerProblems.euler028.euler028 import sum_diagonal


def test_sum_diagonal():
    assert sum_diagonal(5) == 101


if __name__ == '__main__':
    pytest.main()
