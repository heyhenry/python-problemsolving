# Leetcode No. 7: Reverse Integer
# More Info: https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x : int) -> int:
        has_negative = False
        x = list(str(x))
        if x[0] == "-":
            has_negative = True
            x.remove("-")
        x.reverse()
        new_x = abs(int("".join(x)))
        if has_negative:
            new_x = "-" + str(new_x)
            new_x = int(new_x)
        if -2**31 <= new_x <= 2**31 - 1:
            print(new_x)
            return new_x
        print(0)
        return 0

            

test_case_01 = 123
test_case_02 = -123
test_case_03 = 120
test_case_04 = 1534236469

s = Solution()

s.reverse(test_case_01)
s.reverse(test_case_02)
s.reverse(test_case_03)
s.reverse(test_case_04)