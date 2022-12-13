# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

PICK = 2


def guess(pick: int) -> int:
    if pick > PICK:
        return -1
    elif pick < PICK:
        return 1
    else:
        return 0


class Solution:
    def guess_number(self, n: int) -> int:
        if n > 1:
            num = n // 2
        else:
            num = n
        if n < 5:
            delta = 1
        else:
            delta = n // 4

        while True:
            # если 1, то увеличиваем
            if guess(num) == 1:
                num += delta
            # если -1, то уменьшаем
            elif guess(num) == -1:
                num -= delta
            elif guess(num) == 0:
                return num
            if delta > 1:
                delta //= 2


if __name__ == '__main__':
    s = Solution()
    print(s.guessNumber(3))
