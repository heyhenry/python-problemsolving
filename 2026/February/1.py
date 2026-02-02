class Solution:
    # brute force method
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     size = len(nums)
    #     for i in range(size):
    #         for j in range(i+1, size):
    #             if nums[i] + nums[j] == target:
    #                 # log result for checking
    #                 print([i, j])
    #                 return [i, j]

    # two hash map pass method
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        size = len(nums)
        nums_map = {}

        for i in range(size):
            nums_map[nums[i]] = i
        
        for i in range(size):
            complement = target - nums[i]
            if complement in nums_map and nums_map[complement] != i:
                print(i, [nums_map[complement]])
                return [i, nums_map[complement]]

test_case_01 = ([2,7,11,15], 9)
test_case_02 = ([3,2,4], 6)
test_case_03 = ([3,3], 6)

s = Solution()

s.twoSum(test_case_01[0], test_case_01[1])
s.twoSum(test_case_02[0], test_case_02[1])
s.twoSum(test_case_03[0], test_case_03[1])
