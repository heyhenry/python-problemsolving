class Solution:
    def roman_to_int(self, s : str) -> int:
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
        size = len(s)
        result = 0
        skip_flag = False
        for i in range(size):
            if skip_flag:
                skip_flag = False
                continue
            if i != size-1:
                if s[i]+s[i+1] in roman_numerals:
                    result += roman_numerals[s[i]+s[i+1]]
                    skip_flag = True
                else:
                    result += roman_numerals[s[i]]
            else:
                result += roman_numerals[s[i]]
        return result

solution = Solution()

test_case_1 = "III"
test_case_2 = "LVIII"
test_case_3 = "MCMXCIV"

print(solution.roman_to_int(test_case_1))
print(solution.roman_to_int(test_case_2))
print(solution.roman_to_int(test_case_3))