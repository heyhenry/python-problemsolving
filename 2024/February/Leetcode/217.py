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
def containsDuplicate(nums : list[int]) -> bool:

    numbers = {}
    result = False

    for i in nums:
        if i not in numbers:
            numbers[i] = nums.count(i)

    for key, val in numbers.items():
        if val > 1:
            result = True

    return result

def main():
    print(containsDuplicate(nums = [1,2,3,1]))
    print(containsDuplicate(nums = [1,2,3,4]))
    print(containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))

if __name__ == "__main__":
    main()