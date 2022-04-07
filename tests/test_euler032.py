import pytest

from EulerProblems.euler032.euler032 import DigitNum

a = DigitNum()


def test_geter_n():
    assert a.n == 0


def test_setter_n():
    a.n = 123
    assert a.n == 123


if __name__ == '__main__':
    pytest.main()
