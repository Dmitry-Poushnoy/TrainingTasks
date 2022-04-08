def get_sum_pandigital_products():
    """
    Find sum of all unique products which are consist of {1-9} like 39 × 186 = 7254
    :return:
    """
    res_list = []
    d4_set = set()
    for d2 in range(0, 100):
        for d3 in range(0, 10000):
            d4 = d2 * d3
            d_string = str(d2) + str(d3) + str(d4)
            candidate_str_set = set(d_string)
            if len(d_string) == 9 and candidate_str_set == {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                if d4 not in d4_set:
                    res_list.append([d2, d3, d4])
                    d4_set.add(d4)
    return sum([item[2] for item in res_list])


if __name__ == '__main__':
    print(f"Сумма всех пандигитальных произведений: {get_sum_pandigital_products()}")
