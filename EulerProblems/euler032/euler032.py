class DigitNum(int):

    def __init__(self, number: int = 0):
        super().__init__()
        self.__n = number
        self.length = self.get_len(self.__n)
        self.pandigital = self.is_pandigital(self.__n)

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, num):
        self.__n = num

    def length(self):
        return self.length

    @staticmethod
    def get_len(x: int) -> int:
        """
        Calculate number of digits in integer number
        :return: Integer number of digits
        """
        return len(str(x))

    @staticmethod
    def is_pandigital(x: int) -> bool:
        """
        Check if integer number is pandigital
        :param x: Integer number to check for pandigitality
        :return: True if the number is pandigital
        """
        len_for_pandigital = DigitNum.get_len(x)
        list_of_digits = [int(i) for i in str(x)]
        set_of_pandigits = set([i for i in range(1, len_for_pandigital+1)])
        if 0 in list_of_digits or len(list_of_digits) != len(set_of_pandigits):
            return False
        else:
            return set(list_of_digits) == set_of_pandigits


if __name__ == '__main__':
    gen_pandigitals_9 = (DigitNum(i) for i in range(12345678, 87654322) if DigitNum(i).pandigital is True)


