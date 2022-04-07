class DigitNum:

    def __init__(self, number=0):
        self.__n = number

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, num):
        self.__n = num


if __name__ == '__main__':
    x = DigitNum(12)
    x.n = 10
    print(x.n)
