class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        size = len(nums)
        for i in range(size):
            for j in range(i+1, size):
                if nums[i] + nums[j] == target:
                    # log result for checking
                    print([i, j])
                    return [i, j]

test_case_01 = ([2,7,11,15], 9)
test_case_02 = ([3,2,4], 6)
test_case_03 = ([3,3], 6)

s = Solution()

s.twoSum(test_case_01[0], test_case_01[1])
s.twoSum(test_case_02[0], test_case_02[1])
s.twoSum(test_case_03[0], test_case_03[1])
