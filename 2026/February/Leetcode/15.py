# Leetcode No.15: 3 Sum
# More Info: https://leetcode.com/problems/3sum/description/
# Additional Help Used: https://www.geeksforgeeks.org/dsa/two-pointers-technique/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()
        size = len(nums)
        
        for i in range(size):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i+1
            right = size-1
            
            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]

                if total_sum < 0:
                    left += 1
                elif total_sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]: 
                        left += 1
        print(results)
        return results

test_case_01 = [-1,0,1,2,-1,-4]
test_case_02 = [0,1,1]
test_case_03 = [0,0,0]

s = Solution()

s.threeSum(test_case_01)
# s.threeSum(test_case_02)
# s.threeSum(test_case_03)

