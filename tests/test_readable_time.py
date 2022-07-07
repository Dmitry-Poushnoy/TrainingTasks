import pytest

from CodeWars.readable_time import make_readable


def test_make_readable():
    assert make_readable(0) == "00:00:00"


if __name__ == '__main__':
    pytest.main()
