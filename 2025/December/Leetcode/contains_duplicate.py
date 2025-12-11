class Solution:
    def contains_duplicate(self, nums : list[int]) -> bool:
        
        # create a set of unique numbers found from the nums list
        unique_nums = set(nums)
        
        # determine whether the lengths between unique_nums and nums does not match 
        return len(unique_nums) != len(nums)

solution = Solution()

test_case_1 = [1,2,3,1]
test_case_2 = [1,2,3,4]
test_case_3 = [1,1,1,3,3,4,3,2,4,2]

print(solution.contains_duplicate(test_case_1))
print(solution.contains_duplicate(test_case_2))
print(solution.contains_duplicate(test_case_3))