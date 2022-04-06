import pytest

from EulerProblems.euler031.euler031 import all_variants_slow
from EulerProblems.euler031.euler031dynamic import get_list_nominals, make_zero_matrix, find_all_variants


def test_all_variants():
    assert all_variants_slow(1) == 1
    assert all_variants_slow(2) == 2
    assert all_variants_slow(3) == 2
    assert all_variants_slow(4) == 3
    assert all_variants_slow(5) == 4
    assert all_variants_slow(6) == 5
    assert all_variants_slow(7) == 6
    assert all_variants_slow(8) == 7
    assert all_variants_slow(9) == 8
    assert all_variants_slow(10) == 11


def test_get_list_nominals():
    assert get_list_nominals(100) == [1, 2, 5, 10, 20, 50, 100]


def test_make_zero_matrix():
    assert make_zero_matrix(5, 4) == [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_find_all_variants():
    assert find_all_variants(200, 1) == 1
    assert find_all_variants(200, 1) == 1
    assert find_all_variants(200, 2) == 2
    assert find_all_variants(200, 3) == 2
    assert find_all_variants(200, 4) == 3
    assert find_all_variants(200, 5) == 4
    assert find_all_variants(200, 6) == 5
    assert find_all_variants(200, 7) == 6
    assert find_all_variants(200, 8) == 7
    assert find_all_variants(200, 9) == 8
    assert find_all_variants(200, 10) == 11
    assert find_all_variants(200, 20) == 41
    assert find_all_variants(200, 30) == 109


if __name__ == '__main__':
    pytest.main()
