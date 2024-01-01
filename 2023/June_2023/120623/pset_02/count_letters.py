"""
Returns the count of each letter in `s` as a dictionary
Examples (dictionary print order doesn't matter):
count_letters("") -> {}
count_letters("abc") -> {'a' : 1, 'b' : 1, 'c' : 1}
count_letters("aaaa") -> {'a' : 4}
count_letters("ababbcca) -> {'a' : 3, 'b' : 3, 'c' : 2}

Required reading: https://docs.python.org/3/tutorial/datastructures.html#dictionaries. Lmk if you have questions
"""
def count_letters(s : str) -> dict[str, int]:
    
    letter_list = []
    results = {}

    for c in s:
        if c not in letter_list:
            letter_list.append(c)

    for i in letter_list:
        results[i] = s.count(i)

    return results

def main():
    print(count_letters(""))
    print(count_letters("abc"))
    print(count_letters("aaaa"))
    print(count_letters("ababbcca"))

if __name__ == "__main__":
    main()

# Completed

# Resources used:
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# https://www.simplilearn.com/tutorials/python-tutorial/count-in-python#:~:text=Count()%20is%20a%20Python,list%2C%20as%20the%20name%20implies.
# https://www.freecodecamp.org/news/create-a-dictionary-in-python-python-dict-methods/#add