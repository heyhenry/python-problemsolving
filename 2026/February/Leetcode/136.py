# Leetcode No. 136: Single Number
# More Info: https://leetcode.com/problems/single-number/description/

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        unique_nums = set(nums)
        for i in unique_nums:
            if nums.count(i) == 1:
                return i

test_case_01 = [2,2,1]
test_case_02 = [4,1,2,1,2]
test_case_03 = [1]

s = Solution()

s.singleNumber(test_case_01)
s.singleNumber(test_case_02)
s.singleNumber(test_case_03)