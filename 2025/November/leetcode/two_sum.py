class Solution:
    def two_sum(self, nums : list[int], target : int) -> list[int]:
        size = len(nums)
        for i in range(size):
            for j in range(i+1, size):
                if nums[i] + nums[j] == target:
                    return [i, j]
        

solution = Solution()

test_case_1 = ([2,7,11,15], 9)
test_case_2 = ([3,2,4], 6)
test_case_3 = ([3,3], 6)

print(solution.two_sum(test_case_1[0], test_case_1[1])) # [0,1]
print(solution.two_sum(test_case_2[0], test_case_2[1])) # [1,2]
print(solution.two_sum(test_case_3[0], test_case_3[1])) # [0,1]

