"""
Returns the list of each letter of `s` expanded in sequence
Examples:
expansion('test') -> ['t', 'te', 'tes', 'test']
expansion('') -> []
expansion('abccba') -> ['a', 'ab', 'abc', 'abcc', 'abccb', 'abccba']
"""
def expansion(s : str) -> list[str]:
    results = []
    expanded = ""
    for c in s:
        expanded += c
        results.append(expanded)
    return results

print(expansion('test'))
print(expansion(''))
print(expansion('abccba'))