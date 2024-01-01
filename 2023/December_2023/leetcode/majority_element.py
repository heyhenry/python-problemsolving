"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""
def majority_element(nums : list[int]) -> int:

    nums_dict = {}

    for i in nums:
        if i not in nums_dict:
            nums_dict[i] = 0

    for i in nums:
        if i in nums_dict:
            nums_dict[i] += 1

    return max(nums_dict, key=nums_dict.get)

def main():
    print(majority_element([3,2,3]))
    print(majority_element([2,2,1,1,1,2,2]))

if __name__ == "__main__":
    main()