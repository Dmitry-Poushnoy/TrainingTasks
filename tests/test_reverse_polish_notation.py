import pytest

from LeetCode.reverse_polish_notation import Solution


def test_eval_rpn_1():
    assert Solution().eval_rpn(["2", "1", "+", "3", "*"]) == 9


def test_eval_rpn_2():
    assert Solution().eval_rpn(["4", "13", "5", "/", "+"]) == 6


def test_eval_rpn_3():
    assert Solution().eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22


if __name__ == '__main__':
    pytest.main()
