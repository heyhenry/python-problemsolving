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

        # Line below referenced this info: https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
        # ---
        # Explanation for self study: 
        # The lambda is used in the key parameter to create an 'on the go' one off function that is isolated in the space of that intialised lambda.
        # The sorted() function iterates through the item pairings (key,value) of the nums_map.
        # The lambda function's first 'item' before the colon takes in each item as they get iterated and 
        # the 'item' after the colon is the returning result (or expression) which includes a '[1]' in this case to refer to the value in the pairing (key,value) 
        # to be used as the basis for determining the sorting order.
        sorted_nums = sorted(nums_map.items(), key=lambda item:item[1], reverse=True)

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