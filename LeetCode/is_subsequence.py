import re


class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        pattern = "\w*".join(s)
        s = re.search(pattern, t)
        return True if s else False

    def is_sequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        if len(s) == 0: return True
        subsequence = 0
        for i in range(0, len(t)):
            if subsequence <= len(s) - 1 and s[subsequence] == t[i]:
                subsequence += 1
        return subsequence == len(s)


if __name__ == '__main__':
    s = Solution()
    s_word = "acb"
    t_word = "ahbgdc"
    print(s.is_subsequence(s_word, t_word))
    print(s.is_sequence(s_word, t_word))
