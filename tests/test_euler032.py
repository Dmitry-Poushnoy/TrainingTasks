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
    assert DigitNum.is_pandigital(987654321, 9) == True
    assert DigitNum.is_pandigital(1223456789, 9) == False
    assert DigitNum.is_pandigital(1234567, 9) == False
    assert DigitNum.is_pandigital(987653210) == False

def test_lenght():
    x2 = DigitNum(65733)
    assert x2.len == 5
    x2 = DigitNum(6573223)
    assert x2.len == 7


if __name__ == '__main__':
    pytest.main()
