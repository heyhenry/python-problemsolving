"""
1512. Number of Good Pairs

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""
def numIdenticalPairs(nums: list[int]) -> int:

    good_pairs = []

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j] and i < j:
                good_pairs.append('poop')


    return len(good_pairs)

def main():
    print(numIdenticalPairs([1,2,3,1,1,3]))
    print(numIdenticalPairs([1,1,1,1]))
    print(numIdenticalPairs([1,2,3]))

if __name__ == "__main__":
    main()