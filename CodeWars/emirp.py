from itertools import islice


def gen_primes():
    """ Генерирует последовательность простых чисел. Возвращает генератор."""
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def collect_all_primes(n: int) -> set[int]:
    """ Формирует множество всех простых чисел до n включительно"""
    prime_set = set()
    primes_generator = gen_primes()
    prime = 0
    while prime <= n:
        prime = next(primes_generator)
        if prime <= n:
            prime_set.add(prime)
    return prime_set


def find_max_possible_reversed_number(n: int) -> [int]:
    """ Найти максимально возможное число той же размерности, что и n"""
    return int('9' * len(str(n)))


def reverse_set_of_nums(all_primes: set[int]) -> set[int]:
    """ Формируем множество развернутых чисел"""
    set_of_reversed_nums = set()
    for item in all_primes:
        set_of_reversed_nums.add(int(str(item)[::-1]))
    return set_of_reversed_nums


def clear_from_palindroms(only_primes_and_emirps: set[int]) -> set[int]:
    """ Удаляет числа-полиндромы"""
    return {i for i in only_primes_and_emirps if i != int(str(i)[::-1])}


def find_emirp(n: int) -> list[int, int, int]:
    """[amount of emirps in the range(0, n), largest emirp smaller than n, sum of all the emirps of this range]"""
    all_primes = collect_all_primes(find_max_possible_reversed_number(n))
    all_reversed_nums = reverse_set_of_nums(all_primes)
    only_emirps = {i for i in all_primes.intersection(all_reversed_nums) if i <= n}
    only_cleared_emirps = clear_from_palindroms(only_emirps)
    quantity_of_emirps = len(only_cleared_emirps)
    if not quantity_of_emirps:
        return [0, 0, 0]
    else:
        return [quantity_of_emirps, max(only_cleared_emirps), sum(only_cleared_emirps)]


if __name__ == '__main__':
    print(find_emirp(1_000_000))

# 1. Определить количество знаков в n
# 2. Найти все простые числа от 0 до 9999 (найденное количество знаков п.1)
# 3. Сгенерировать множество развёрнутых чисел из множества п.2
# 4. Сформировать пересечение множеств п.2 и п.3
# 5. Отсортировать множество п.4
# 6. Ставить только числа <= n
# 7. Избавиться от палиндромов
# 8. Найти кол-во, максимальное, сумму развернутых чисел
