class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+ 1, len(nums)):
                if nums[i] + nums[j] == target:
                    print([i,j])
                    return [i,j]


solution = Solution()
solution.twoSum(nums = [2,7,11,15], target = 9)
solution.twoSum(nums = [3,2,4], target = 6)
solution.twoSum(nums = [3,3], target = 6)