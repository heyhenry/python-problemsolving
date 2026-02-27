# Leetcode No.13: Roman to Integer
# More Info: https://leetcode.com/problems/roman-to-integer/description/

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
        for i in range(len(s)):
            if skip_flag:
                skip_flag = False
                continue
            if i != len(s) - 1:
                if s[i] + s[i+1] in roman_numerals:
                    result += roman_numerals[s[i]+s[i+1]]
                    skip_flag = True
                else:
                    result += roman_numerals[s[i]]
            else:
                result += roman_numerals[s[i]]

        return result

test_case_01 = "III"
test_case_02 = "LVIII"
test_case_03 = "MCMXCIV"

s = Solution()

print(s.romanToInt(test_case_01))
print(s.romanToInt(test_case_02))
print(s.romanToInt(test_case_03))