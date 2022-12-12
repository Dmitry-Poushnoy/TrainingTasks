import pytest as pytest

from CodeWars.format_duration import format_duration


def test_format_duration_0():
    assert format_duration(0) == "now"


def test_format_duration_1():
    assert format_duration(1) == "1 second"

    # def test_format_duration_62():
    assert format_duration(62) == "1 minute and 2 seconds"


def test_format_duration_120():
    assert format_duration(120) == "2 minutes"


def test_format_duration_3600():
    assert format_duration(3600) == "1 hour"


def test_format_duration_3662():
    assert format_duration(3662) == "1 hour, 1 minute and 2 seconds"


if __name__ == '__main__':
    pytest.main()
