# Задача: Каждая цифра представлена в виде буквы. Известно, что КРЯКВА+КРЯ+КРЯ делится на 167
# без остатка. Докажите любым способом (а лучше двумя), что КВАКРЯ+КВА+КВА не делится на 167.


def is_krjkva(krjkva: int) -> bool:
    krjkva_list = list(str(krjkva))
    len6 = bool(len(krjkva_list) == 6)
    k_eq = bool(krjkva_list[0] == krjkva_list[3])
    others = bool(len({krjkva_list[i] for i in range(len(krjkva_list)) if i not in {0, 3}}) == 4)
    return all((len6, k_eq, others))


def krj(krjkva: int) -> int:
    return int(str(krjkva)[:3])


def kva(krjkva: int) -> int:
    return int(str(krjkva)[3:])


def kvakrj(krjkva: int) -> int:
    return int("".join([str(krjkva)[3:], str(krjkva)[:3]]))


if __name__ == '__main__':
    for i in range(100000, 999999):
        if is_krjkva(i):
            if (i + 2 * krj(i)) % 167 == 0:
                print(f"{i} + {krj(i)} + {krj(i)} / 167 = {(i + 2 * krj(i))/167}"
                      f"     {kvakrj(i)} + {kva(i)} + {kva(i)} / 167 = {(kvakrj(i) + 2* kva(i)) / 167}")
