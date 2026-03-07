# Leetcode No.3: Longest Substring Without Repeating Characters
# More Info: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_arrays = []
        sub_string = ""
        for c in s:
            if c not in sub_string:
                sub_string += c
            else:
                sub_arrays.append(sub_string)
                c_index = sub_string.rfind(c)
                sub_string = sub_string[c_index+1:] + c
        if sub_string not in sub_arrays:
            sub_arrays.append(sub_string)
        return len(max(sub_arrays, key=len))

test_case_01 = "abcabcbb"
test_case_02 = "bbbbb"
test_case_03 = "pwwkew"

s = Solution()

print(s.lengthOfLongestSubstring(test_case_01))
print(s.lengthOfLongestSubstring(test_case_02))
print(s.lengthOfLongestSubstring(test_case_03))