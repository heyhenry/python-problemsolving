"""
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true
"""
def contains_duplicates(nums : list[int]) -> bool:
    # use set() method to find all the unique digits in the nums list
    unique_nums = set(nums)
    # check to see if the length is the same between unique_nums and nums
    return len(unique_nums) != len(nums)

def main():
    print(contains_duplicates(nums = [1,2,3,1]))
    print(contains_duplicates(nums = [1,2,3,4]))
    print(contains_duplicates(nums = [1,1,1,3,3,4,3,2,4,2]))

if __name__ == "__main__":
    main()