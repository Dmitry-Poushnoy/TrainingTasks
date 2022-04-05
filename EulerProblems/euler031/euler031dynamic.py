# a[i][j] - это количество вариантов набрать сумму j
#           с помощью монет максимальным номиналом v[j],
#           где v=[1, 2, 5, 10, 20, 50, 100, 200]
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
    for columns in range(amount):
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
    print(f"{str((POSSIBLE_NOMINALS)[len(matrix[0])-1]).rjust(4)}")
    for _ in range(len(matrix[0])+1):
        print('-----', end='')
    print('\n')
    for ind_col, val_col in enumerate(matrix):
        print(f"{str(ind_col+1).rjust(3)}|", end='')
        for ind_row, val_row in enumerate(val_col):
            print(f"{str(val_row).rjust(4)}", end=' ')
        print(f"\n")


if __name__ == '__main__':
    a = make_zero_matrix(200, 200)
    print_matrix(a)
