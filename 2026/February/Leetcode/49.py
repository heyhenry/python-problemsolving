# Leetcode No.49 Group Anagrams
# More Info: https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        strs_map = {}
        results = []
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in strs_map:
                strs_map[sorted_s] = [s]
            else:
                strs_map[sorted_s].append(s)

        for v in strs_map.values():
            results.append(v)

        print(results)
        return results


test_case_01 = ["eat","tea","tan","ate","nat","bat"]
test_case_02 = [""]
test_case_03 = ["a"]

s = Solution()

s.groupAnagrams(test_case_01)
# s.groupAnagrams(test_case_02)
# s.groupAnagrams(test_case_03)