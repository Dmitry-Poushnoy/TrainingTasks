import pytest

from EulerProblems.euler032.euler032 import get_sum_pandigital_products


def test_get_sum_pandigital_products():
    assert get_sum_pandigital_products() == 45228


if __name__ == '__main__':
    pytest.main()
