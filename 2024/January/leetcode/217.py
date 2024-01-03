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
def containsDuplicate(nums: list[int]) -> bool:

    # solution 1
    # result = False

    # nums_dict = {}

    # for i in nums:
    #     if i not in nums_dict:
    #         nums_dict[i] = nums.count(i)
    
    # for key, value in nums_dict.items():
    #     if value > 1:
    #         result = True

    # return result

    # solution 2 (also faster and does not exceed leetcode time limit)
    result = False

    uni = set()

    for i in nums:
        if i not in uni:
            uni.add(i)
        else:
            result = True
            break

    return result

def main():
    print(containsDuplicate([1,2,3,1]))
    print(containsDuplicate([1,2,3,4]))
    print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

if __name__ == "__main__":
    main()