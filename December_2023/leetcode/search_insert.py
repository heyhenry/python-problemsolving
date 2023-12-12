"""
5. Search Insert Position

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

    index_position = -1
    find_position = -1

    for i in range(len(nums)):
        if nums[i] == target:
            index_position = i
    
    if index_position == -1:

        for i in range(len(nums)):
            if target > i:
                index_position += 1
                if i == (len(nums)-1):
                    index_position += 1
        
    return index_position

def main():
    print(search_insert([1,3,5,6],5))
    print(search_insert([1,3,5,6],2))
    print(search_insert([1,3,5,6],7))

if __name__ == "__main__":
    main()