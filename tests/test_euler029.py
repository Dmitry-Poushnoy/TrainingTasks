import pytest as pytest

from EulerProblems.euler029.euler029 import func


def test_func():
    assert func() == False


if __name__ == '__main__':
    pytest.main()
