"""
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.


Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""
# # solution 1
# def single_number(nums : list[int]) -> int:

#     result = 0
#     nums_dict = {}
#     unique_nums = []

#     # stores all the unique nums into a list
#     for i in nums:
#         if i not in unique_nums:
#             unique_nums.append(i)

#     # iterates through the unique_nums list and finds the count for each number based on the given nums list
#     for i in unique_nums:
#         nums_dict[i] = nums.count(i)

#     # searches for the number that only have a single instance
#     for key, val in nums_dict.items():
#         if val == 1:
#             # when number with single instance is found, is stored in the result variable
#             result = key

#     return result

# solution 2 - reduced code lines by condensing steps (based on solution 1)
def single_number(nums : list[int]) -> int:

    result = 0
    nums_dict = {}

    for i in nums:
        if i not in nums_dict:
            nums_dict[i] = nums.count(i)
    
    for key, val in nums_dict.items():
        if val == 1:
            result = key

    return result

def main():
    print(single_number([2,2,1]))
    print(single_number([4,1,2,1,2]))
    print(single_number([1]))

if __name__ == "__main__":
    main()