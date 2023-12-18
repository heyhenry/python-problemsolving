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
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""
def roman_to_int(s : str) -> int:

    # contains all the relevant value and their references
    roman_numerals = {"I": 1, "V": 5, "L": 50, "M": 1000, "CM": 900, "XC": 90, "IV": 4}

    skip_iteration = -1
    result = 0

    for chr in range(len(s)):
        
        # if index equals skip_iteration, it means it was used in the previous loop, so skip it
        # to avoid duplicate indexing
        if chr == skip_iteration:
            skip_iteration = 0
            continue
        
        # if the index is not the last index in the list 
        # to account for the future indexing scheme for 2 character references
        if chr != len(s)-1:
            # check to see if it's a 2 character reference value
            if s[chr] + s[chr+1] == "CM" or s[chr] + s[chr+1] == "XC" or s[chr] + s[chr+1] == "IV":
                # if so, reference dictionary for the relevant value
                result += roman_numerals[s[chr]+s[chr+1]]
                # record the used index that needs to be skipped
                skip_iteration = chr+1
            # else if it isnt a 2 character reference, then find the appropriate single reference and its value
            else:
                result += roman_numerals[s[chr]]
        # find the appropriate single reference and its value, as its the last char
        # and has been confirmed not to be apart of a 2 character reference
        else:
            result += roman_numerals[s[chr]]

    return result


def main():
    print(roman_to_int("III"))
    print(roman_to_int("LVIII"))
    print(roman_to_int("MCMXCIV"))

if __name__ == "__main__":
    main()