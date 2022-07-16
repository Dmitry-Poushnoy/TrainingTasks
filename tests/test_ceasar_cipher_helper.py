import pytest

from CodeWars.caesar_cipher_helper import CaesarCipher


def test_encode():
    assert CaesarCipher(5).encode('Codewars') == 'HTIJBFWX'


if __name__ == '__main__':
    pytest.main()
