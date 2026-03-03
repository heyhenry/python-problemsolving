# Leetcode No.49: Group Anagrams
# More Info: https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        for a in strs:
            sorted_a = "".join(sorted(a))
            if sorted_a not in anagrams:
                anagrams[sorted_a] = [a]
            else:
                anagrams[sorted_a].append(a)
        
        results = []
        for vals in anagrams.values():
            results.append(vals)
        return results

test_case_01 = ["eat","tea","tan","ate","nat","bat"]
test_case_02 = [""]
test_case_03 = ["a"]

s = Solution()

print(s.groupAnagrams(test_case_01))
print(s.groupAnagrams(test_case_02))
print(s.groupAnagrams(test_case_03))