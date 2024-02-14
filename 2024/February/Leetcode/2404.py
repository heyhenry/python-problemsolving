"""
2404. Most Frequent Even Element

Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1.

 

Example 1:

Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.
Example 2:

Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.
Example 3:

Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element.
 

Constraints:

1 <= nums.length <= 2000
0 <= nums[i] <= 105
"""
def mostFrequentEven(nums : list[int]) -> int:

    result = -1

    x = set(nums)

    numbers = {}

    for i in x:
        if i % 2 == 0:
            numbers[i] = nums.count(i)
    
    if len(numbers) > 1:

        max_num = max(numbers.values())
        winners = []
        
        for key, val in numbers.items():
            if val == max_num:
                winners.append(key)

        result = min(winners)
    
    elif len(numbers) == 1:
        
        num = list(numbers)
        result = num[0]

    return result

def main():
    print(mostFrequentEven(nums = [0,1,2,2,4,4,1]))
    print(mostFrequentEven(nums = [4,4,4,9,2,4]))
    print(mostFrequentEven(nums = [29,47,21,41,13,37,25,7]))

if __name__ == '__main__':
    main()