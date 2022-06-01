import pytest

from CodeWars.domain_name import domain_name


def test_domain_name():
    assert domain_name("http://google.com") == "google"
    # assert domain_name("http://google.co.jp") == "google"
    # assert domain_name("www.xakep.ru") == "xakep"
    # assert domain_name("https://youtube.com") == "youtube"


if __name__ == '__main__':
    pytest.main()
