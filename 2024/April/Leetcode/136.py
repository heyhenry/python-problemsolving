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

    for i in n:
        if nums.count(i) < 2:
            return i

def main():
    print(single_number(nums = [2,2,1]))
    print(single_number(nums = [4,1,2,1,2]))
    print(single_number(nums = [1]))

if __name__ == "__main__":
    main()