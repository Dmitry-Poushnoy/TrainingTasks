import pytest

from CodeWars.move_zeros import move_zeros


def test_move_zeroes():
    assert move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]


if __name__ == '__main__':
    pytest.main()
