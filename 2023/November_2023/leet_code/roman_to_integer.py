"""
13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
import sys 

def roman_to_int(s : str) -> int:
    
    result = 0
    counter = 0

    for c in range(len(s)):
        if counter == len(s):
            break
        if s[c] == 'L': 
            result += 50
            counter += 1
        elif s[c] == 'V':
            result += 5
            counter += 1
        elif s[c] == 'I':
            if c != len(s) - 1:
                if s[c+1] == 'V':
                    result += 4
                    counter += 2
                else:
                    result += 1
                    counter += 1
            else:
                result += 1
                counter += 1
        elif s[c] == 'M':
            if c == 0:
                result += 1000
                counter += 1
            elif s[c-1] == 'C':
                result += 900
                counter += 2
        elif s[c] == 'X':
            if c != len(s) - 1:
                if s[c+1] == 'C':
                    result += 90
                    counter += 2

    return result
            
def main():

    print(roman_to_int('III'))
    print(roman_to_int('LVIII'))
    print(roman_to_int('MCMXCIV'))

    # # Non-embedded version
    # result = sys.argv[1]
    # print(roman_to_int(result))

if __name__ == "__main__":
    main()