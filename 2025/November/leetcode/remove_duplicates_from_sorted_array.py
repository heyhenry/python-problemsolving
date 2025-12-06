class Solution:
    def remove_duplicates(self, nums : list[int]) -> int:
        # first method 
        k = sorted(list(set(nums)))
        nums.clear()
        nums += k
        return len(k)

solution = Solution()

test_case_1 = [1,1,2]
test_case_2 = [0,0,1,1,1,2,2,3,3,4]

print(solution.remove_duplicates(test_case_1))
print(solution.remove_duplicates(test_case_2))