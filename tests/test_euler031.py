import pytest

from EulerProblems.euler031.euler031 import tmp_func


def test_tmp_func():
    assert tmp_func() == False


if __name__ == '__main__':
    pytest.main()
