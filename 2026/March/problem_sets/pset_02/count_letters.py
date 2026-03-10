""" 
  Returns the count of each letter in `s` as a dictionary 
 
  Examples (dictionary print order doesn't matter): 
    count_letters("") -> {} 
    count_letters("abc") -> {'a' : 1, 'b' : 1, 'c' : 1} 
    count_letters("aaaa") -> {'a' : 4} 
    count_letters("ababbcca") -> {'a' : 3, 'b' : 3, 'c' : 2} 
"""
def count_letters(s : str) -> dict[str, int]: 
    # end the function early if string is empty
    if len(s) < 1:
        return {}
    
    # initiate a dictionary to store character counts
    letters_map = {}
    # return a list (or set in here) of all unique characters found in s string
    unique_chars = set(s)

    # loop through all the unique characters
    for c in unique_chars:
        # create new keys with respective counts for each character
        letters_map[c] = s.count(c)
    
    # return results
    return letters_map

test_cases = [
    "",
    "abc",
    "aaaa",
    "ababbcca"
]

for i in test_cases:
    print(count_letters(i))