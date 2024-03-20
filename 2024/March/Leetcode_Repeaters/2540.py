"""
2540. Minimum Common Value

Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.
Example 2:

Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
 

Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[j] <= 109
Both nums1 and nums2 are sorted in non-decreasing order.
"""
def get_common(nums1 : list[int], nums2 : list[int]) -> int:

    result = -1
    n = len(max(nums1, nums2, key=len))

    for i in range(n):
        if nums1[i] in nums2:
            result = nums1[i]
            break

    return result

def main():
    print(get_common(nums1 = [1,2,3], nums2 = [2,4]))
    print(get_common(nums1 = [1,2,3,6], nums2 = [2,3,4,5]))

if __name__ == "__main__":
    main()