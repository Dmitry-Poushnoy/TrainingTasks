import pytest

from CodeWars.krjkva import is_krjkva, krj, kva, kvakrj


def test_is_krjkva():
    assert is_krjkva(123156) == True
    assert is_krjkva(123456) == False


def test_krj():
    assert krj(123456) == 123
    assert krj(923456) == 923


def test_kva():
    assert kva(123456) == 456
    assert kva(923451) == 451


def test_kvakrj():
    assert kvakrj(123145) == 145123


if __name__ == '__main__':
    pytest.main()
