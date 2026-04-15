"""
Returns the list of each letter of `s` expanded in sequence
Examples:
expansion('test') -> ['t', 'te', 'tes', 'test']
expansion('') -> []
expansion('abccba') -> ['a', 'ab', 'abc', 'abcc', 'abccb', 'abccba']
"""
def expansion(s : str) -> list[str]:
    results = []
    expand = ""
    for c in s:
        expand += c
        results.append(expand)
    return results

print(expansion('test'))
print(expansion(''))
print(expansion('abccba'))