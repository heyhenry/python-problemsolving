# Leetcode No.347: Top K Frequent Elements
# More Info: https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        nums_map = {}
        for i in nums:
            if i not in nums_map:
                nums_map[i] = 1
            else:
                nums_map[i] += 1

        # line below referenced this info: https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
        sorted_nums = sorted(nums_map.items(), key=lambda x:x[1], reverse=True)

        results = []
        for i in sorted_nums[:k]:
            results.append(i[0])

        print(results)
        return results

s = Solution()

test_case_01 = ([1,1,1,2,2,3], 2)
test_case_02 = ([1], 1)
test_case_03 = ([1,2,1,2,1,2,3,1,3,2], 2)

s.topKFrequent(test_case_01[0], test_case_01[1])
s.topKFrequent(test_case_02[0], test_case_02[1])
s.topKFrequent(test_case_03[0], test_case_03[1])