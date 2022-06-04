def next_bigger(n: int) -> int:
    n_members = [i for i in str(n)]
    n_members_sorted = [i for i in sorted(n_members, reverse=True)]
    if n_members == n_members_sorted:
        return -1
    max_number = int(''.join(n_members_sorted))
    for i in range(n + 1, max_number + 1):
        i_members = [j for j in str(i)]
        if sorted(i_members, reverse=True) == n_members_sorted:
            return i


if __name__ == '__main__':
    print(next_bigger(4219))
