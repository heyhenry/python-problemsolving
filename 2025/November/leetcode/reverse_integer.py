class Solution:
    def reverse(self, x : int) -> int:
        x = str(x)
        s = x[::-1]
        if "-" in x:
            s = s.replace("-", "")
            s = -abs(int(s))
        else:
            s = int(s)
        if (s < -2**31) or (s > (2**31 - 1)):
            return 0
        return s

solution = Solution()

test_case_1 = 123
test_case_2 = -123
test_case_3 = 120

print(solution.reverse(test_case_1))
print(solution.reverse(test_case_2))
print(solution.reverse(test_case_3))