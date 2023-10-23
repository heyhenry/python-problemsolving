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
def second_vowel(s : str) -> int:

    result = -1
    counter = 0

    for c in range(len(s)):
        if s[c] in 'aeiou' or (s[c] == 'y' and c != 0):
            counter += 1
        if counter == 2:
            result = c
    
    return result

def main():
    print(second_vowel('test'))
    print(second_vowel('aeiou'))
    print(second_vowel('slowly'))
    print(second_vowel('yip'))
    print(second_vowel('pygmy'))
    print(second_vowel('yppy'))

if __name__ == "__main__":
    main()
