class Solution:
    # solution 1 - discovered on my own
    def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     for i in range(len(nums)):
    #         for j in range(i+ 1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 print([i,j])
    #                 return [i,j]

    # solution 2 - saw from Solutions Tab (credit: Rahul Varma), written after understanding each line clearly (shown by comments)
    # Writing from memory..
        # outline variables
        num_map = {}
        # storing list length in variable reduces compute time
        size = len(nums)

        # populate the dictionary
        for i in range(size):
            num_map[nums[i]] = i

        # algorithm
        for i in range(size):
            complement = target - nums[i]
            if complement in num_map and num_map[complement] != i:
                print([i, num_map[complement]])
                return [i, num_map[complement]] 

solution = Solution()
solution.twoSum(nums = [2,7,11,15], target = 9)
solution.twoSum(nums = [3,2,4], target = 6)
solution.twoSum(nums = [3,3], target = 6)