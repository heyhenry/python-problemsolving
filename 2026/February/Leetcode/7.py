# Leetcode No. 7: Reverse Integer
# More Info: https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x : int) -> int:
        x = str(x)
        print(x[::-1])
        return x[::-1]

test_case_01 = 123
test_case_02 = -123
test_case_03 = 120

s = Solution()

s.reverse(test_case_01)
s.reverse(test_case_02)
s.reverse(test_case_03)
