# Leetcode No.9: Palindrome Number
# More Info: https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        print(x == x[::-1])
        return x == x[::-1]

test_case_01 = 121
test_case_02 = -121
test_case_03 = 10

s = Solution()

s.isPalindrome(test_case_01)
s.isPalindrome(test_case_02)
s.isPalindrome(test_case_03)