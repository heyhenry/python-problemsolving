nums = [2, 7, 11, 15]
target = 9
numMap = {}
n = len(nums)
for i in range(n):
    numMap[nums[i]] = i

for i in range(n):
    complement = target - nums[i]
    if complement in numMap and numMap[complement] != i:
        print([i, numMap[complement]])
 