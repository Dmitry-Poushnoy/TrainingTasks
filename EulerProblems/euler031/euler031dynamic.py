POSSIBLE_NOMINALS = (1, 2, 5, 10, 20, 50, 100, 200)


def get_list_nominals(max_nominal: int) -> list[int]:
    """
    Get list of nominals where maximum nominal is less than or equal max_nominal
    :param max_nominal: Max nominal of coin
    :return: List of possible nominals of coins.
    """
    return [i for i in POSSIBLE_NOMINALS if i <= max_nominal]


def make_zero_matrix(max_nominal: int, amount: int):
    """
    Make a matrix of zeroes, where columns are nominals and rows are number of coins each of nominals
    :param max_nominal: Max nominal of coins
    :param amount: Sum of money (number of coins)
    :return: 2D matrix of zeroes
    """
    v = get_list_nominals(max_nominal)
    res_matrix = []
    for columns in range(amount + 1):
        res_matrix.append([])
        for rows in v:
            res_matrix[columns].append(0)
    return res_matrix


def print_matrix(matrix: list[int]):
    """
    Print the matrix
    :param matrix: 2D matrix
    """
    print("    ", end='')
    for _ in range(len(matrix[0]) - 1):
        print(f"{str((POSSIBLE_NOMINALS)[_]).rjust(4)}", end=' ')
    print(f"{str((POSSIBLE_NOMINALS)[len(matrix[0]) - 1]).rjust(4)}")
    for _ in range(len(matrix[0]) + 1):
        print('-----', end='')
    print('\n')
    for ind_col, val_col in enumerate(matrix):
        print(f"{str(ind_col + 1).rjust(3)}|", end='')
        for ind_row, val_row in enumerate(val_col):
            print(f"{str(val_row).rjust(4)}", end=' ')
        print(f"\n")


def find_all_variants(max_nominal: int, amount: int) -> int:
    # a[i][j] - это количество вариантов набрать сумму j
    # с помощью монет максимальным номиналом v[i],
    # где v=[1, 2, 5, 10, 20, 50, 100, 200]
    a = make_zero_matrix(max_nominal, amount)
    v = get_list_nominals(max_nominal)
    for i in range(amount + 1):
        a[i][0] = 1
        for j, j_val in enumerate(v):
            if i == 0:
                a[i][j] = 1
            elif j > 0:
                if i - j_val < 0:
                    j_val = 0
                a[i][j] = a[i][j - 1] + a[i - j_val][j]
    else:
        return a[amount][len(v) - 1]


if __name__ == '__main__':
    max_nominal = int(input("Введите максимальный номинал монеты: "))
    amount = int(input("Введите сумму (в пенсах): "))
    b = find_all_variants(max_nominal, amount)
    print(f"Количество разных вариантов набрать сумму: {b}")
