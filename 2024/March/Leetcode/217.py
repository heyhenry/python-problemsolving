"""
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
def contains_duplicates(nums : list[int]) -> bool:

    n = set(nums)

    return len(n) != len(nums)

def main():
    print(contains_duplicates(nums = [1,2,3,1]))
    print(contains_duplicates(nums = [1,2,3,4]))
    print(contains_duplicates(nums = [1,1,1,3,3,4,3,2,4,2]))

if __name__ == "__main__":
    main()