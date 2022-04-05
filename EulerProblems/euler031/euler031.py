import itertools


def get_max_nominal(amount: int) -> int:
    """
    Finds the maximum nominal of coin for amount of pennies
    :param amount: Amount of pennies
    :return: Maximum nominal of coin
    """
    nominals = (200, 100, 50, 20, 10, 5, 2, 1)
    for nominal in nominals:
        if amount >= nominal:
            return nominal
    else:
        return 0


def get_list_nominals(max_nominal: int) -> list[int]:
    """
    Get list of possible nominals of coins
    :param max_nominal:
    :return: list of possible nominals of coins
    """
    nominals = (200, 100, 50, 20, 10, 5, 2, 1)
    return [nom for nom in nominals if nom <= max_nominal]


def get_optimal_members(amount: int, list_nominals: list[int]) -> list[list[int]]:
    """
    Find optimal list of "nominal * number of coins"
    :param amount: Amount of pennies
    :param list_nominals: List of nominals
    :return: List of "nominal * number of coins"
    """
    res_list = []
    reminder = amount
    number_of_coins = 0
    while reminder:
        if reminder > list_nominals[0]:
            number_of_coins += 1
            reminder -= list_nominals[0]
        elif reminder == list_nominals[0]:
            number_of_coins += 1
            res_list.append([list_nominals[0], number_of_coins])
            return res_list
        else:
            if number_of_coins >0:
                res_list.append([list_nominals[0], number_of_coins])
            list_nominals.pop(0)
            number_of_coins = 0
    return res_list


def all_variants_slow(amount: int) -> int:
    """
    Calculates how many variants of coin sets are available for the given amount of pennies.
    :param amount: Amount of pennies to calculate variants for.
    :return: variants of coins sets
    """
    nominals = (200, 100, 50, 20, 10, 5, 2, 1)
    res_sum = 0
    for j in range(amount, 0, -1):
        print(j)
        res_sum += len([i for i in itertools.combinations_with_replacement(nominals, j) if sum(i) == amount])
    return res_sum


if __name__ == '__main__':
    print(f"{11} - {all_variants_slow(11)}")
