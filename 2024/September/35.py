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
"""
def search_insert(nums, target):

    size = len(nums)

    if target < nums[0]:
        return 0
    elif target > nums[-1]:
        return len(nums)

    for i in range(size):
        if nums[i] == target:
            return i
        elif i < size-1 and target > nums[i] and target < nums[i+1]:
            return i+1

def main():
    print(search_insert(nums = [1,3,5,6], target = 5))
    print(search_insert(nums = [1,3,5,6], target = 2))
    print(search_insert(nums = [1,3,5,6], target = 7))

if __name__ == "__main__":
    main()