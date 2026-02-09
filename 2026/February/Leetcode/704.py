# Leetcode No.704: Binary Search
# More Info: https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                print(i)
                return i
        print(-1)
        return -1

test_case_01 = ([-1,0,3,5,9,12], 9)
test_case_02 = ([-1,0,3,5,9,12], 2)

s = Solution()

s.search(test_case_01[0], test_case_01[1])
s.search(test_case_02[0], test_case_02[1])