class Solution:
    def is_ugly(self, n: int) -> bool:
        for p in 2, 3, 5:
            while n % p == 0 < n:
                n /= p
        return n == 1


if __name__ == '__main__':
    s = Solution()
    print(s.is_ugly(100))
