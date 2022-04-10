from fractions import Fraction
from functools import reduce


def possible_numerators(end: int) -> list[int]:
    """
    Make list of numbers more than 10 and which haven't zeroes at last digit and which don't have equal digigs.
    :param end: Maximum int
    :return: List of 2-digits integers without zeroes at last digit and without equal lsat two digits
    """
    return [i for i in range(10, end) if (i % 10 != 0) and (i % 11 != 0) and 0 < i < 100]


def get_common_digit(a: int, b: int) -> list[int]:
    """
    Find the same digits in numbers
    :param a: First number
    :param b: Second number
    :return: Common digit
    """
    a_str, b_str = str(a), str(b)
    res_list = []
    for i in a_str:
        if i in b_str:
            res_list.append(int(i))
    return res_list


def get_1digit_list(a: int, b: int, c: int) -> list[int]:
    """
    Produce a list of 1-digit numerator and denominator by removing equal digits
    :param a: numerator
    :param b: denominator
    :param c: Common digit
    :return: List of 1-digit numerator and denominator
    """
    a, b, c = map(str, (a, b, c))
    a_1digit = int(a.replace(c, ''))
    b_1digit = int(b.replace(c, ''))
    return [a_1digit, b_1digit] if a_1digit < b_1digit else [0, 1]


if __name__ == '__main__':
    non_trivials = []
    for numerator in possible_numerators(99):
        for denominator in possible_numerators(100):
            common_digit = get_common_digit(numerator, denominator)
            if numerator < denominator and len(common_digit) == 1:
                old_fraction = Fraction(numerator, denominator)
                fraction_1digit_components = get_1digit_list(numerator, denominator, common_digit[0])
                new_fraction = Fraction(fraction_1digit_components[0], fraction_1digit_components[1])
                if old_fraction == new_fraction:
                    non_trivials.append(Fraction(numerator, denominator))
    print(*non_trivials)
    res = reduce(lambda x, y: x * y, non_trivials)
    print(res)
    print(f"The answer is {res.denominator}")
