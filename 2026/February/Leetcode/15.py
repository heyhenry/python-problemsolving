# Leetcode No.15: 3 Sum
# More Info: https://leetcode.com/problems/3sum/description/
# Additional Help Used: https://www.geeksforgeeks.org/dsa/two-pointers-technique/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()
        size = len(nums)
        
        for i in range(size):
            # Checks the values of the indexes i and the previous one starting for duplicate values, 
            # which will lead to an automatic skip of the index iteration at hand.
            # It will start checking the conditions of the index's after the first iteration.
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i+1
            right = size-1
            
            while left < right:
                # Provides the initial summed total to be used for comparison and 2 pointer adjustment.
                total_sum = nums[i] + nums[left] + nums[right]

                # Adjust the required pointer (left or right) based on the value of the summed total.
                if total_sum < 0:
                    left += 1
                elif total_sum > 0:
                    right -= 1
                else:
                    # Stores the valid triplet in the results list
                    results.append([nums[i], nums[left], nums[right]])
                    # Will continue to the next element moving from the left index.
                    left += 1
                    # If a duplicate value is found, then it will skip and continue going
                    # through the elements until a non-duplicate value is found,
                    # then it will break the inner while loop and resume the outer while loop.
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

