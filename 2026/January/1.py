# 1. Two Sum

class Solution:
    # method: brute force
    # def two_sum(self, nums: list[int], target: int) -> list[int]:
    #     # brute force method:
    #     size = len(nums)
    #     for i in range(size):
    #         for j in range(i+1, size):
    #             if nums[i] + nums[j] == target:
    #                 # result log
    #                 print([i, j])
    #                 return [i, j]
    #     # should never be prompted based on problem's constraints, just a style choice
    #     return

    # method: single pass
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        size = len(nums)
        num_map = {}
        for i in range(size):
            # get a remainder number with current iteration's value provided by the nums' list
            complement = target - nums[i]
            # check if the remainder number already exists in the num_map, 
            # if it does that means this current iteration's value + remainder number is the 
            # first valid result that equals the given target value
            if complement in num_map:
                # print statement to check the result
                print([num_map[complement], i])
                return [num_map[complement], i]
            # if the conditional if statement is not met, add the current iteration's value to the num_map
            num_map[nums[i]] = i
        # dummy return for aesthetics, based on details, there will always be a match found
        return 

s = Solution()

test_case_1 = ([2,7,11,15], 9) # answer: [0,1]
test_case_2 = ([3,2,4], 6) # answer: [1,2]
test_case_3 = ([3,3], 6) # answer: [0,1]

s.two_sum(test_case_1[0], test_case_1[1])
s.two_sum(test_case_2[0], test_case_2[1])
s.two_sum(test_case_3[0], test_case_3[1])
