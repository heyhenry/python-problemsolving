""" 
  Returns the count of each letter in `s` as a dictionary 
 
  Examples (dictionary print order doesn't matter): 
    count_letters("") -> {} 
    count_letters("abc") -> {'a' : 1, 'b' : 1, 'c' : 1} 
    count_letters("aaaa") -> {'a' : 4} 
    count_letters("ababbcca") -> {'a' : 3, 'b' : 3, 'c' : 2} 
"""
def count_letters(s : str) -> dict[str, int]: 
    letters_dict = {}
    for c in s:
        if c not in letters_dict:
            letters_dict[c] = 1
        else:
            letters_dict[c] += 1
    return letters_dict

test_cases = [
    "",
    "abc",
    "aaaa",
    "ababbcca"
]

for i in test_cases:
    print(count_letters(i))