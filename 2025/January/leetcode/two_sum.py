class Solution:
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # solution 1 - discovered on my own
        # for i in range(len(nums)):
        #     for j in range(i+ 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             print([i,j])
        #             return [i,j]

        # solution 2 - saw from Solutions Tab (credit: Rahul Varma), written after understanding each line clearly (shown by comments)
        # Writing from memory..
        # # outline variables
        # num_map = {}
        # # storing list length in variable reduces compute time
        # size = len(nums)

        # # populate the dictionary
        # for i in range(size):
        #     num_map[nums[i]] = i

        # # algorithm
        for i in range(size):
            # find a value that makes up the target value alongside the current looped number value
            complement = target - nums[i]
            # if the found value (complement) is found inside the populated num_map..
            if complement in num_map and num_map[complement] != i:
                # then it is deemed to have found a valid make up of 2 elements in the nums list to equal the target value
                return [i, num_map[complement]]
        
        # solution 3 - single dictionary iteration
        num_map = {}
        size = len(nums)

        for i in range(size):
            complement = target - nums[i]
            if complement in num_map:
                return [num_map[complement], i]
            num_map[nums[i]] = i
        

solution = Solution()
print(solution.twoSum(nums = [2,7,11,15], target = 9))
solution.twoSum(nums = [3,2,4], target = 6)
solution.twoSum(nums = [3,3], target = 6)