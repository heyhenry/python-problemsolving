# Returns the index of the second vowel in `s`
# If no vowels are in `s`, returns -1
# A vowel is defined to be 'aeiou', and a 'y' that _isn't_ the first character
# Examples:
# second_vowel('test') -> -1
# second_vowel('aeiou') -> 1
# second_vowel('slowly') -> -1
# second_vowel('yip') -> -1

def second_vowel(s : str) -> int:

    vowels = ['a', 'e', 'i', 'o', 'u']
    counter = 0
    y_counter = 0
    result = -1

    for letter in range(len(s)):

        if s[letter] in vowels:
            counter +=1
        if s[letter] == 'y' and letter > 0:
            counter += 1
        if counter == 2:
            result = letter
    
    return result

def main():
    print(second_vowel('test')) # -1
    print(second_vowel('aeiou')) # 1
    print(second_vowel('slowly')) # 5
    print(second_vowel('yip')) # -1
    print(second_vowel('zzaz')) # -1
    print(second_vowel('zzyzzy')) # 2
    print(second_vowel('yzzyzzzzy')) # 8

if __name__ == "__main__":
    main()