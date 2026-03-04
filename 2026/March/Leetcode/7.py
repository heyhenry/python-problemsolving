# Leetcode No.7: Reverse Integer
# More Info: https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        contains_negative = False
        if x < 0:
            contains_negative = True
        x = str(x)[::-1].replace("-", "")
        if contains_negative:
            x = "-" + x 
        x = int(x)
        if -2**31 <= x <= (2**31-1):
            return x
        return 0

test_case_01 = 123
test_case_02 = -321
test_case_03 = 120

s = Solution()

print(s.reverse(test_case_01))
print(s.reverse(test_case_02))
print(s.reverse(test_case_03))