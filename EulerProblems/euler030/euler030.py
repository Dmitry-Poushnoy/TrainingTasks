def is_power_number(number: int, power: int) -> bool:
    """
    Check if the number is sum of powers of its digits
    :param number: Number
    :param power: To what power to raise
    :return: True if the number is sum of powers
    """
    if number == 1:
        return False
    list_number = list(map(int, str(number)))
    calc_sum = sum(i ** power for i in list_number)
    return number == calc_sum


def sum_power_numbers(power: int) -> int:
    """
    Summarize power numbers
    :param power: Power
    :return: Sum of power numbers
    """
    max_pow = 9 ** power
    max_number = max_pow * len(str(max_pow))
    sum_res = 0
    for i in range(1, max_number):
        if is_power_number(i, power):
            sum_res += i
    return sum_res


if __name__ == '__main__':
    print(sum_power_numbers(5))
