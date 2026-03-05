# Leetcode No.125: Valid Palindrome
# More Info: https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""
        for c in s:
            if c.isalnum():
                clean_s += c.lower()
        return clean_s == clean_s[::-1]

test_case_01 = "A man, a plan, a canal: Panama"
test_case_02 = "race a car"
test_case_03 = " "

s = Solution()

print(s.isPalindrome(test_case_01))
print(s.isPalindrome(test_case_02))
print(s.isPalindrome(test_case_03))