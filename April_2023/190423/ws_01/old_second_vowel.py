def second_vowel(s : str) -> int:

    vowel_counter = 0
    index_counter = -1

    for alpha in s:
        index_counter += 1
        if alpha == 'a':
            vowel_counter += 1
        elif alpha == 'e':
            vowel_counter += 1
        elif alpha == 'i':
            vowel_counter += 1
        elif alpha == 'o':
            vowel_counter += 1
        elif alpha == 'u':
            vowel_counter += 1
        elif alpha == 'y' and alpha is not s[0]:
            vowel_counter += 1

        if vowel_counter == 2:
            return index_counter
            
    return -1

def main():
    print(second_vowel('test')) # -1
    print(second_vowel('aeiou')) # 1
    print(second_vowel('slowly')) # 5
    print(second_vowel('yip')) # -1
    print(second_vowel('zzaz')) # -1
    print(second_vowel('zzyzzy')) # 2
    print(second_vowel('zzyzzyzzy'))

if __name__ == "__main__":
    main()

# Take-away notes after comparing with the new solution
# --------
# This old solution I wrote does not consider finding the next possible instance of a 'y' that is not the first letter in a string, 
# rather it finds the second 'y' instance that also excluding counting any potential first element that is 'y'.