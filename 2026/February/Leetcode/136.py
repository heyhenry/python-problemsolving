# Leetcode No. 136: Single Number
# More Info: https://leetcode.com/problems/single-number/description/

class Solution:

    # solved using set() to find all nums and count() to find the number that had a sum of 1
    def singleNumber(self, nums: list[int]) -> int:
        unique_nums = set(nums)
        for i in unique_nums:
            if nums.count(i) == 1:
                return i
    
    # solved using dict as a counter and list as a filter
    def singleNumber(self, nums: list[int]) -> int:
        nums_dict = {}
        smallest_number = []
        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = 1
            else:
                nums_dict[i] += 1
            if nums_dict[i] == 1:
                smallest_number.append(i)
            else:
                smallest_number.remove(i)
        
        print(smallest_number[0])
        return smallest_number[0]
    
    # solved using bit manipulation technique using XOR bitwise operator
    def singleNumber(self, nums: list[int]) -> int:
        a = 0
        for i in nums:
            a = a ^ i
        
        print(a)
        return a

test_case_01 = [2,2,1]
test_case_02 = [4,1,2,1,2]
test_case_03 = [1]

s = Solution()

s.singleNumber(test_case_01)
s.singleNumber(test_case_02)
s.singleNumber(test_case_03)