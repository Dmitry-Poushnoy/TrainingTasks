import pytest as pytest

from EulerProblems.euler030.euler030 import func


def test_func():
    assert func() == False


if __name__ == '__main__':
    pytest.main()
