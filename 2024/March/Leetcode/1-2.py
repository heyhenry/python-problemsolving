"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
def two_sum(nums : list[int], target : int) -> list[int]:

    og_nums = []
    og_nums += nums
    n = len(nums)
    result = []
    left, right = 0, n-1
    nums.sort()

    while len(result) < 2:
        
        ans = nums[left] + nums[right]

        if ans > target:
            right -= 1
        elif ans < target:
            left += 1
        else:
            for i in range(len(og_nums)):
                if og_nums[i] == nums[left]:
                    result.append(i)
            for i in range(len(og_nums)):
                if og_nums[i] == nums[right] and i not in result:
                    result.append(i)
            
    return result

def main():
    print(two_sum(nums = [2,7,11,15], target = 9))
    print(two_sum(nums = [3,2,4], target = 6))
    print(two_sum(nums = [3,3], target = 6))

if __name__ == "__main__":
    main()