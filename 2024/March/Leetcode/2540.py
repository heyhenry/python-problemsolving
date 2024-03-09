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
def get_common(nums1 : list[int], nums2: list[int]) -> int:

    result = -1
    set1 = set(nums1)
    set2 = set(nums2)
    common = list(set1.intersection(set2))
    if len(common) > 0:
        result = min(common)
    return result

def main():
    print(get_common(nums1 = [1,2,3], nums2 = [2,4]))
    print(get_common(nums1 = [1,2,3,6], nums2 = [2,3,4,5]))
    print(get_common([1,2,8,12,32,34,43,52,57,62,64,67,71,71,79,81,86,91,93,94],[9,11,12,14,19,25,29,31,38,39,41,42,58,63,66,70,71,73,91,91])) # 12

if __name__ == "__main__":
    main()