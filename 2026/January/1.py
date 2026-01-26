# 1. Two Sum

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        # brute force method:
        size = len(nums)
        for i in range(size):
            for j in range(i+1, size):
                if nums[i] + nums[j] == target:
                    # result log
                    print([i, j])
                    return [i, j]
        # should never be prompted based on problem's constraints, just a style choice
        return

s = Solution()

test_case_1 = ([2,7,11,15], 9) # answer: [0,1]
test_case_2 = ([3,2,4], 6) # answer: [1,2]
test_case_3 = ([3,3], 6) # answer: [0,1]

s.two_sum(test_case_1[0], test_case_1[1])
s.two_sum(test_case_2[0], test_case_2[1])
s.two_sum(test_case_3[0], test_case_3[1])
