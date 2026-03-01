# Leetcode No.1: Two Sum
# More Info: https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # method: brute force
        # size = len(nums)
        # for i in range(size):
        #     for j in range(i+1, size):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # method: one pass
        # num_map = {}
        
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in num_map:
        #         return [num_map[complement], i]
        #     num_map[nums[i]] = i

        # method: two pass
        num_map = {}
        size = len(nums)

        for i in range(size):
            num_map[nums[i]] = i
        
        for i in range(size):
            complement = target - nums[i]
            if complement in num_map and num_map[complement] != i:
                return [i, num_map[complement]]

test_case_01 = ([2,7,11,15], 9)
test_case_02 = ([3,2,4], 6)
test_case_03 = ([3,3], 6)

s = Solution()

print(s.twoSum(test_case_01[0], test_case_01[1]))
print(s.twoSum(test_case_02[0], test_case_02[1]))
print(s.twoSum(test_case_03[0], test_case_03[1]))