import string


class CaesarCipher(object):
    def __init__(self, shift: int):
        self.shift = self.verified_shift(shift)

    @classmethod
    def verified_shift(cls, shift):
        if 0 < shift < 27:
            return shift
        else:
            raise ValueError("Сдвиг должен быть в диапазоне от 1 до 26")

    def encode(self, st: str) -> str:
        # print(f"Исходное: {st:>16}")
        escapes = ''.join([chr(char) for char in range(1, 32)])
        translator = str.maketrans('', '', escapes)
        st = st.translate(translator)
        # print(f"После удаления: {st:>10}")
        res = ''
        for letter in st:
            if letter in string.punctuation + ' ':
                res += letter
            else:
                if ord(letter) + self.shift > 122:
                    res += chr(ord(letter) + self.shift - 26).upper()
                else:
                    res += chr(ord(letter) + self.shift).upper()
        # print(f"Закодированное: {res:>10}")
        return res

    def decode(self, st: str) -> str:
        res = ''
        for letter in st:
            if letter in string.punctuation + ' ':
                res += letter
            else:
                if ord(letter) - self.shift < 65:
                    res += chr(ord(letter) - self.shift + 26)
                else:
                    res += chr(ord(letter) - self.shift)
        # print(f"Раскодированное: {res:>9} \n")
        return res


if __name__ == '__main__':
    c = CaesarCipher(5)
    c.encode('Codewars')
    c.decode('HTIJBFWX')

