"""
Returns the index of the second vowel in `s`
If no vowels are in `s`, returns -1
A vowel is defined to be 'aeiou', and a 'y' that _isn't_ the first character
Examples:
second_vowel('test') -> -1
second_vowel('aeiou') -> 1
second_vowel('slowly') -> 5
second_vowel('yip') -> -1
"""
class Problem:
    def second_vowel(self, s : str) -> int:
        vowels = "aeiou"
        vowel_counter = 0
        for i in range(len(s)):
            if s[i] in vowels or (vowel_counter >= 1 and s[i] == "y"):
                vowel_counter += 1
            if vowel_counter == 2:
                return i
        return -1

test_01 = "test"
test_02 = "aeiou"
test_03 = "slowly"
test_04 = "yip"

p = Problem()

print(p.second_vowel(test_01))
print(p.second_vowel(test_02))
print(p.second_vowel(test_03))
print(p.second_vowel(test_04))
