class Solution:
    def contains_duplicate(self, nums : list[int]) -> bool:
        size = len(nums)
        unique_size = len(set(nums))
        return size != unique_size

solution = Solution()

test_case_1 = [1,2,3,1]
test_case_2 = [1,2,3,4]
test_case_3 = [1,1,1,3,3,4,3,2,4,2]

print(solution.contains_duplicate(test_case_1)) # true
print(solution.contains_duplicate(test_case_2)) # false
print(solution.contains_duplicate(test_case_3)) # true
