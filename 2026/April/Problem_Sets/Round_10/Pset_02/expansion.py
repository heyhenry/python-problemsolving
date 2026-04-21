"""
Returns the list of each letter of `s` expanded in sequence
Examples:
expansion('test') -> ['t', 'te', 'tes', 'test']
expansion('') -> []
expansion('abccba') -> ['a', 'ab', 'abc', 'abcc', 'abccb', 'abccba']
"""
def expansion(s : str) -> list[str]:
    result = ""
    results = []
    for c in s:
        result += c
        results.append(result)
    return results

print(expansion('test'))
print(expansion(''))
print(expansion('abccba'))