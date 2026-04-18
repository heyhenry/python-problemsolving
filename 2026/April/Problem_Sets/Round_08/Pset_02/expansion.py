"""
Returns the list of each letter of `s` expanded in sequence
Examples:
expansion('test') -> ['t', 'te', 'tes', 'test']
expansion('') -> []
expansion('abccba') -> ['a', 'ab', 'abc', 'abcc', 'abccb', 'abccba']
"""
def expansion(s : str) -> list[str]:
    if len(s) < 1:
        return []
    results = [s[0]]
    for c in range(1, len(s)):
        results.append(results[-1]+s[c])
    return results

print(expansion('test'))
print(expansion(''))
print(expansion('abccba'))