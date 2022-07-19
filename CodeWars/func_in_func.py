def zero(*args):
    if len(args) == 0:
        return 0
    return eval(f"0{args[0]}")


def one(*args):
    if len(args) == 0:
        return 1
    return eval(f"1{args[0]}")


def two(*args):
    if len(args) == 0:
        return 2
    return eval(f"2{args[0]}")


def three(*args):
    if len(args) == 0:
        return 3
    return eval(f"3{args[0]}")


def four(*args):
    if len(args) == 0:
        return 4
    return eval(f"4{args[0]}")


def five(*args):
    if len(args) == 0:
        return 5
    return eval(f"5{args[0]}")


def six(*args):
    if len(args) == 0:
        return 6
    return eval(f"6{args[0]}")


def seven(*args):
    if len(args) == 0:
        return 7
    return eval(f"7{args[0]}")


def eight(*args):
    if len(args) == 0:
        return 8
    return eval(f"8{args[0]}")


def nine(*args):
    if len(args) == 0:
        return 9
    return eval(f"9{args[0]}")


def plus(num):
    return f"+{num}"


def minus(num):
    return f"-{num}"


def times(num):
    return f"*{num}"


def divided_by(num):
    return f"//{num}"


if __name__ == '__main__':
    print(two(plus(three())))
    print(two(minus(three())))
    print(two(times(three())))
    print(two(divided_by(three())))
