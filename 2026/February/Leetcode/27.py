# Leetcode No. 27: Remove Element
# More Info: https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        lst = []
        for i in nums:
            if i != val:
                lst.append(i)
        nums.clear()
        nums += lst
        return len(nums)

test_case_01 = ([3,2,2,3], 3)
test_case_02 = ([0,1,2,2,3,0,4,2], 2)

s = Solution()

print(s.removeElement(test_case_01[0], test_case_01[1]))
print(s.removeElement(test_case_02[0], test_case_02[1]))