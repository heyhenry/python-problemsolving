class Solution:
    def reverse(self, x : int) -> int:
        
        # reverse the given x excluding any existing negatives
        reversed_x = str(x).strip("-")[::-1]
        
        # add the negative if it pre-existed
        if len(reversed_x) != len(str(x)):
            # add the negative via string concatenation
            reversed_x = "-"+reversed_x

        # convert final value (reversed integer) to type int
        reversed_x = int(reversed_x)

        # check if the reversed integer value is within the signed 32-bit integer range
        if reversed_x > -2**31 and reversed_x < (2**31 - 1):
            # if within the signed 32-bit integer range, then return reversed integer value
            return reversed_x
        
        # if outside the signed 32-bit integer range, then return 0
        return 0


solution = Solution()

test_case_1 = 123
test_case_2 = -123
test_case_3 = 120

print(solution.reverse(test_case_1))
print(solution.reverse(test_case_2))
print(solution.reverse(test_case_3))
