# Leetcode No.3: Longest Substring Without Repeating Characters
# More Info: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_strs = []
        substr = ""
        for c in s:
            if c not in substr:
                substr += c
            else:
                sub_strs.append(substr)
                # first instance of c before this current loop
                c_index = substr.rfind(c)
                substr = substr[c_index+1:] + c
        if substr not in sub_strs:
            sub_strs.append(substr)

        print(max(sub_strs, key=len))
        # print(len(max(sub_strs)))
        return (max(sub_strs, key=len))

test_case_01 = "abcabcbb"
test_case_02 = "bbbbb"
test_case_03 = "pwwkew"

s = Solution()

s.lengthOfLongestSubstring(test_case_01)
s.lengthOfLongestSubstring(test_case_02)
s.lengthOfLongestSubstring(test_case_03)