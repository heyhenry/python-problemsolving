"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
def search_insert(nums : list[int], target : int) -> int:

    n = len(nums)
    result = -1

    if target > nums[n-1]:
        result = n
    elif target < nums[0]:
        result = 0
    else:
        for i in range(n):
            if target == nums[i]:
                result = i
                break
            elif i != n-1 and target > nums[i] and target < nums[i+1]:
                result = i+1
                break
            elif i != 0 and target < nums[i] and target > nums[i-1]:
                result = i
                break
            
    return result

def main():
    print(search_insert(nums = [1,3,5,6], target = 5))
    print(search_insert(nums = [1,3,5,6], target = 2))
    print(search_insert(nums = [1,3,5,6], target = 7))

if __name__ == "__main__":
    main()