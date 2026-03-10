# Leetcode No.13: Roman to Integer
# More Info: https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            "I": 1,
            "V": 5,
            "IV": 4,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }

        result = 0
        skip_flag = False
        for c in range(len(s)):
            if skip_flag:
                skip_flag = False
                continue
            if c != len(s) - 1:
                if s[c]+s[c+1] in roman_numerals:
                    result += roman_numerals[s[c]+s[c+1]]
                    skip_flag = True
                else:
                    result += roman_numerals[s[c]]
            else:
                result += roman_numerals[s[c]]
        return result

test_cases = [
    "III",
    "LVIII",
    "MCMXCIV"
]

s = Solution()

for i in test_cases:
    print(s.romanToInt(i))