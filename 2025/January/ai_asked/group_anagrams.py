"""
Problem 1: Grouping Anagrams

Write a function that takes a list of strings and groups them into lists of anagrams. 
Two strings are anagrams if they contain the same characters in the same frequency, regardless of order.
"""
def group_anagrams(words : list[str]) -> list[list[str]]:
    result = []
    sorted_words = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in sorted_words:
            sorted_words[sorted_word] = [word]
        elif sorted_word in sorted_words:
            sorted_words[sorted_word].append(word)
    for val in sorted_words.values():
        result.append(val)
    return result
            

print(group_anagrams(["listen", "silent", "enlist", "rat", "tar", "art", "cat", "tac", "act"]))
# Result:
# [
#     ["listen", "silent", "enlist"],
#     ["rat", "tar", "art"],
#     ["cat", "tac", "act"]
# ]