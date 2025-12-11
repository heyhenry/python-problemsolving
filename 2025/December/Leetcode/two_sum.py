class Solution:
    def two_sum(self, nums : list[int], target: int) -> list[int]:
        # brute force method
        # size = len(nums)
        # for i in range(size):
        #     for j in range(i+1, size):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return
    
        # two pass method
        size = len(nums)
        num_maps = {}
        
        # first pass 
        # intentionally loop over existing integer values with latest one found in the nums list
        for i in range(size):
            num_maps[nums[i]] = i

        for i in range(size):
            # find the complement integer value that makes up the other half of the target's sum
            complement = target - nums[i]
            # check if the complement is in nums_map,
            # once the first check is cleared, proceed to check if the value (index) located at the provided key 
            # (complement) does not match with the index of the current iteration's i (index) in nums[i] (aka the other half of the target's sum)
            if complement in num_maps and num_maps[complement] != i:
                # return the indexes of the two values that total the target's value
                return [num_maps[complement], i]
        
        return

solution = Solution()

test_case_1 = ([2,7,11,15], 9)
test_case_2 = ([3,2,4], 6)
test_case_3 = ([3,3], 6)

print(solution.two_sum(test_case_1[0], test_case_1[1]))
# print(solution.two_sum(test_case_2[0], test_case_2[1]))
# print(solution.two_sum(test_case_3[0], test_case_3[1]))