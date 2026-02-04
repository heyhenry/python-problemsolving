# Leetcode No.125: Valid Palindrome
# More Info: https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    # method 1
    # def isPalindrome(self, s: str) -> bool:
    #     new_s = ""
    #     for c in s:
    #         if c.isalnum():
    #             new_s += c.lower()
    #     # to log result
    #     print(new_s == new_s[::-1])    
    #     return new_s == new_s[::-1]
    
    # method 2 (just less lines)
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        s = "".join(s)
        print(s == s[::-1])
        return s == s[::-1]

test_case_01 = "A man, a plan, a canal: Panama"
test_case_02 = "race a car"
test_case_03 = " "

s = Solution()

s.isPalindrome(test_case_01)
s.isPalindrome(test_case_02)
s.isPalindrome(test_case_03)