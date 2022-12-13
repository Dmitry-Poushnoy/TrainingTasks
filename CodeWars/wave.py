# 1.  The input string will always be lower case but maybe empty.
# 2.  If the character in the string is whitespace then pass over it as if it was an empty seat

def wave(people: str) -> list[str]:
    people = people.lower()
    res = []
    for idx, val in enumerate(people):
        if val == ' ':
            continue
        up_letter = people[idx].upper()
        res.append(people[:idx] + up_letter + people[idx + 1:])
    return res


if __name__ == '__main__':
    # wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
    print(wave("hello friend"))
