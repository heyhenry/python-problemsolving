# Leetcode No.704: Binary Search
# More Info: https://leetcode.com/problems/binary-search/description/

class Solution:
    # def search(self, nums: list[int], target: int) -> int:
    #     for i in range(len(nums)):
    #         if nums[i] == target:
    #             print(i)
    #             return i
    #     print(-1)
    #     return -1

    # the binary search method way
    def search(self, nums: list[int], target: int) -> int:
        size = len(nums)
        left = 0
        right = size-1
        # continue loop while left's value is less than or equal to right's value
        while left <= right:
            # find the middle of the list
            mid = (left + right) // 2
            if nums[mid] == target:
                print(mid)
                return mid
            # find the new left value, which will be used in the next iteration for the new middle
            elif nums[mid] < target:
                left = mid + 1
            # find the new right value, which will be used in the next iteration for the new middle
            elif nums[mid] > target:
                right = mid - 1
        print(-1)
        return -1

test_case_01 = ([-1,0,3,5,9,12], 9)
test_case_02 = ([-1,0,3,5,9,12], 2)

s = Solution()

s.search(test_case_01[0], test_case_01[1])
s.search(test_case_02[0], test_case_02[1])