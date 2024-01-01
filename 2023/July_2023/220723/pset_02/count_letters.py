"""
Returns the count of each letter in `s` as a dictionary
Examples (dictionary print order doesn't matter):
count_letters("") -> {}
count_letters("abc") -> {'a' : 1, 'b' : 1, 'c' : 1}
count_letters("aaaa") -> {'a' : 4}
count_letters("ababbcca) -> {'a' : 3, 'b' : 3, 'c' : 2}
"""
def count_letters(s : str) -> dict[str, int]:

    letters = []

    for c in s:
        if c not in letters:
            letters.append(c)
    
    letters_dict = {}

    for i in letters:
        letters_dict[i] = s.count(i)

    return letters_dict

def main():
    print(count_letters(""))
    print(count_letters("abc"))
    print(count_letters("aaaa"))
    print(count_letters("ababbcca"))

if __name__ == "__main__":
    main()