# Leetcode No.217: Contains Duplicate
# More Info: https://leetcode.com/problems/contains-duplicate/description/

class Solution:

    # # new list method
    # def containsDuplicate(self, nums: list[int]) -> bool:
    #     unique_nums = []

    #     for i in nums:
    #         if i not in unique_nums:
    #             unique_nums.append(i)
    #         else:
    #             print("True")
    #             return True
    #     print("False")
    #     return False

    # set() comparison method
    def containsDuplicate(self, nums: list[int]) -> bool:
        print(len(nums) != len(set(nums)))
        # comparing original list against set() version of list
        return len(nums) != len(set(nums))

s = Solution()

test_case_01 = [1,2,3,1]
test_case_02 = [1,2,3,4]
test_case_03 = [1,1,1,3,3,4,3,2,4,2]

s.containsDuplicate(test_case_01) # true
s.containsDuplicate(test_case_02) # false 
s.containsDuplicate(test_case_03) # true