"""
88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""
def merge(nums1 : list[int], m : int, nums2 : list[int], n : int) -> None:

    temp = []
    sub_a = []
    sub_b = []

    for i in range(len(nums1)):

        sub_a.append(nums1[i])
        if i+1 == m:
            break

    for i in range(len(nums2)):

        sub_b.append(nums2[i])
        if i+1 == n:
            break

    if len(sub_a) == 1 and 0 in sub_a:
        temp += sub_b
    else:
        temp += sub_a
        temp += sub_b

    temp.sort()

    nums1.clear()
    nums1 += temp

def main():
    
    # test case 1
    test1_nums1 = [1,2,3,0,0,0]
    test1_nums2 = [2,5,6]
    test1_m = 3
    test1_n = 3

    print(test1_nums1)
    merge(test1_nums1, test1_m, test1_nums2, test1_n)
    print(test1_nums1)

    print('---')
    # test case 2
    test2_nums1 = [1]
    test2_nums2 = []
    test2_m = 1
    test2_n = 0

    print(test2_nums1)
    merge(test2_nums1, test2_m, test2_nums2, test2_n)
    print(test2_nums1)

    print('---')
    # test case 3
    test3_nums1 = [0]
    test3_nums2 = [1]
    test3_m = 0
    test3_n = 1

    print(test3_nums1)
    merge(test3_nums1, test3_m, test3_nums2, test3_n)
    print(test3_nums1)

if __name__ == '__main__':
    main()