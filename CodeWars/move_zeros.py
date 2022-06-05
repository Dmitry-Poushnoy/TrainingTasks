def move_zeros(array: list[int]) -> list[int]:
    res_list = [i for i in array if i != 0]
    count_zeros = array.count(0)
    for i in range(count_zeros):
        res_list.append(0)
    return res_list


if __name__ == '__main__':
    print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
