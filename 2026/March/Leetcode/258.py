# Leetcode No.258: Add Digits
# More Info: https://leetcode.com/problems/add-digits/description/

class Solution:
    def add_digits(self, num: int) -> int:
        while True:
            result = 0
            for i in str(num):
                result += int(i)
            if result < 10:
                return result
            else:
                num = result

test_cases = [
    38,
    0
]

s = Solution()

for test in test_cases:
    print(s.add_digits(test))