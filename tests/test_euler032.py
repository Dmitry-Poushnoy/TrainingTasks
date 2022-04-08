import pytest

from EulerProblems.euler032.euler032 import DigitNum


def test_geter_n():
    a = DigitNum()
    assert a.n == 0


def test_setter_n():
    a = DigitNum()
    a.n = 123
    assert a.n == 123


def test_is_pandigital():
    assert DigitNum.is_pandigital(987654321) == True
    assert DigitNum.is_pandigital(13) == False
    assert DigitNum.is_pandigital(132) == True
    assert DigitNum.is_pandigital(1223456789) == False
    assert DigitNum.is_pandigital(1734562) == True
    assert DigitNum.is_pandigital(987653210) == False
    assert DigitNum.is_pandigital(123456790) == False

def test_length():
    x2 = DigitNum(65733)
    assert x2.length == 5


if __name__ == '__main__':
    pytest.main()
