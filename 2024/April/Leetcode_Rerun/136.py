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
def single_number(nums : list[int]) -> int:

    n = set(nums)
    d = {}

    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 2

    for key, val in d.items():
        if val == 1:
            return key

def main():
    print(single_number())
    print(single_number())
    print(single_number())

if __name__ == "__main__":
    main()