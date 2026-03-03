# Leetcode No. 217: Contains Duplicate
# More Info: https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # method 1: using set()
        # unique_nums = set(nums)
        # return len(unique_nums) != len(nums)

        # tested and learnt that writing the above code like this reads a faster runtime.
        return len(set(nums)) != len(nums)
        
test_case_01 = [1,2,3,1]
test_case_02 = [1,2,3,4]
test_case_03 = [1,1,1,3,3,4,3,2,4,2]

s = Solution()

print(s.containsDuplicate(test_case_01))
print(s.containsDuplicate(test_case_02))
print(s.containsDuplicate(test_case_03))