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
def vowel_checker(c : chr):
    
    vowels = ['a', 'e', 'i', 'o', 'u']

    if c in vowels:
        return True
    
    return False

def second_vowel(s : str) -> int:

    vowel_counter = 0

    for c in range(len(s)):
        if vowel_checker(s[c]):
            vowel_counter += 1
            if vowel_counter == 2:
                return c
        if s[c] == 'y' and c != 0:
            vowel_counter += 1
            if vowel_counter == 2:
                return c

    return -1

def main():
    print(second_vowel('test'))
    print(second_vowel('aeiou'))
    print(second_vowel('slowly'))
    print(second_vowel('yip'))
    print(second_vowel('yppy'))
    print(second_vowel('yippy'))
    print(second_vowel('pygmy'))

if __name__ == "__main__":
    main()

# Completed