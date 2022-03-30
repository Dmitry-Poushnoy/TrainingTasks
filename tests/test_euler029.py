import pytest as pytest

from EulerProblems.euler029.euler029 import distinct_seq


def test_distinct_seq():
    assert distinct_seq(2, 5, 2, 5) == 15


if __name__ == '__main__':
    pytest.main()
