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
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
def majority_element(nums: list[int]) -> int:

    result = 0

    for i in nums:
        if nums.count(i) >= len(nums)/2:
            result = i

    return result

def main():
    print(majority_element([3,2,3]))
    print(majority_element([2,2,1,1,1,2,2]))

if __name__ == "__main__":
    main()