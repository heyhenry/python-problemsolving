"""
1588. Sum of All Odd Length Subarrays

Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
Example 2:

Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
Example 3:

Input: arr = [10,11,12]
Output: 66
 

Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= 1000
 

Follow up:

Could you solve this problem in O(n) time complexity?
"""
def sumOddLengthSubarrays(arr : list[int]) -> int:

    # sub_arrs = []

    # for i in range(len(arr)):
    #     for j in range(i+1, len(arr)+1):
    #         sub_arrs.append(arr[i:j])

    # result = 0

    # for i in sub_arrs:
    #     if len(i) % 2 != 0:
    #         for j in i:
    #             result += j

    # return result

# had to look at the first for loop section of my previous solution to get it. 
# still struggling to remember and understand the line 'sub_arrs.append(arr[i:j])' independently without testing to see output
    
    result = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            if len(arr[i:j]) % 2 != 0:
                result += sum(arr[i:j])

    return result

def main():
    print(sumOddLengthSubarrays(arr = [1,4,2,5,3]))
    print(sumOddLengthSubarrays(arr = [1,2]))
    print(sumOddLengthSubarrays(arr = [10,11,12]))

if __name__ == "__main__":
    main()