"""
219. Contains Duplicate II

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 
Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""
def contains_nearby_duplicate(nums: list[int], k: int) -> bool:

    result = False

    # nums[i] == nums[j] and abs(i - j) <= k
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and abs(i - j) <= k:
                result = True
    
    return result

def main():
    print(contains_nearby_duplicate([1,2,3,1],3))
    print(contains_nearby_duplicate([1,0,1,1],1))
    print(contains_nearby_duplicate([1,2,3,1,2,3],2))

if __name__ == "__main__":
    main()