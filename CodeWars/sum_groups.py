from itertools import groupby


def sum_groups(arr: list[int]) -> int:
    new_arr = [list(key) for group, key in groupby(arr, lambda x: x % 2)]
    return len(new_arr)


if __name__ == '__main__':
    arr = [1, 3, 5, 2, 4, 6, 2, 4, 1, 3, 2, 4, 1]
    print(sum_groups(arr))
