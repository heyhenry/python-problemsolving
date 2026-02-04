# Leetcode No.125: Valid Palindrome
# More Info: https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c.lower()
        # to log result
        print(new_s == new_s[::-1])    
        return new_s == new_s[::-1]
    
test_case_01 = "A man, a plan, a canal: Panama"
test_case_02 = "race a car"
test_case_03 = " "

s = Solution()

s.isPalindrome(test_case_01)
s.isPalindrome(test_case_02)
s.isPalindrome(test_case_03)