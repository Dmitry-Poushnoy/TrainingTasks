import pytest

from CodeWars.anagrams import anagrams


def test_anagrams():
    assert anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa']
    assert anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer']


if __name__ == '__main__':
    pytest.main()
