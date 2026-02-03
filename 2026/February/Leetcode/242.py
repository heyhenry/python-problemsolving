# Leetcode No.242: Valid Anagram
# More Info: https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t = "".join(sorted(t))
        s = "".join(sorted(s))
        print(s == t)
        return s == t

s = Solution()

test_case_01 = ("anagram", "nagaram")
test_case_02 = ("rat", "car")

s.isAnagram(test_case_01[0], test_case_01[1])
s.isAnagram(test_case_02[0], test_case_02[1])