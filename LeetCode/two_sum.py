class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        for _ind, _val in enumerate(nums):
            second_num = target - _val
            if second_num in nums and nums.index(second_num) != _ind:
                return [_ind, nums.index(second_num)]


if __name__ == '__main__':
    res = Solution()
    print(res.two_sum([3, 2, 4], 6))

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
