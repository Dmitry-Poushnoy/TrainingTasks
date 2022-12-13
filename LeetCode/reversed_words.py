class Solution:
    def reverse_words(self, s: str) -> str:
        return " ".join(reversed(s.strip().split()))

if __name__ == '__main__':
    res = Solution()
    print(res.reverse_words("the sky is blue"))