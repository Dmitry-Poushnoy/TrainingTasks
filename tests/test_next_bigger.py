import pytest

from CodeWars.next_bigger import next_bigger


def test_next_bigger():
    assert next_bigger(12) == 21


if __name__ == '__main__':
    pytest.main()
