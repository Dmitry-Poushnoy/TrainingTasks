def sum_of_4steps(start: int, step: int) -> int:
    '''
    Calculates sum of 4 numbers by step
    :param start: Start number
    :param step: Step between consequence numbers
    :return:
    '''
    return 4*start + 6*step


def sum_diagonal(matrix_len: int) -> int:
    '''
    Calculates the sum of diagonal elements
    :param matrix_len: Number of rows of the quadratic matrix
    :return: Sum of diagonal elements
    '''
    total_sum = 1
    start, step = 3, 2
    while step <= matrix_len - 1:
        total_sum += sum_of_4steps(start, step)
        start += 4 * step + 2
        step += 2
    return total_sum


if __name__ == '__main__':
    print(sum_diagonal(1001))
