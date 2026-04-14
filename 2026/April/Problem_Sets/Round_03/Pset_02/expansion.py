"""
Returns the list of each letter of `s` expanded in sequence
Examples:
expansion('test') -> ['t', 'te', 'tes', 'test']
expansion('') -> []
expansion('abccba') -> ['a', 'ab', 'abc', 'abcc', 'abccb', 'abccba']
"""
def expansion(s : str) -> list[str]:
    expanded_s = ""
    results = []
    for c in s:
        expanded_s += c
        results.append(expanded_s)
    return results

print(expansion('test'))
print(expansion(''))
print(expansion('abccba'))