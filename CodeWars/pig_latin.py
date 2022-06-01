import string


def pig_it(text: str) -> str:
    res = str()
    for word in text.split():
        if word in string.punctuation:
            res += word + ' '
        elif word[-1] not in string.punctuation:
            res += word[1:] + word[0] + 'ay '
        else:
            res += word[1:-1] + word[0] + 'ay' + word[-1] + ' '
    return res[:-1]
    # lst = text.split()
    # return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])


if __name__ == '__main__':
    print(pig_it('O tempora o mores, comnation !'))
    print("Oay emporatay oay mores, omnationcay !")
