class DigitNum:

    def __init__(self, number: int = 0):
        self.__n = number
        self.len = self.get_len(self.__n)
        self.pandigital = self.is_pandigital(self.__n, self.len)

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, num):
        self.__n = num

    @staticmethod
    def get_len(x: int) -> int:
        """
        Calculate number of digits in integer number
        :return: Integer number of digits
        """
        return len([i for i in str(x)])

    @staticmethod
    def is_pandigital(x: int, len_for_pandigital: int = 9) -> bool:
        '''
        Check if integer number is pandigital
        :param x: Integer number to check for pandigitality
        :param len_for_pandigital: Number for checking (int from 1 to 9)
        :return: True if the number is pandigital
        '''
        list_of_digits = [i for i in str(x)]
        if '0' in list_of_digits or len(list_of_digits) != len_for_pandigital:
            return False
        return len(set(list_of_digits)) == len_for_pandigital


if __name__ == '__main__':
    pass
