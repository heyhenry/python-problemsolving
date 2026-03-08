"""
Returns the list of each letter of `s` expanded in sequence
Examples:
expansion('test') -> ['t', 'te', 'tes', 'test']
expansion('') -> []
expansion('abccba') -> ['a', 'ab', 'abc', 'abcc', 'abccb', 'abccba']
"""
def expansion(s : str) -> list[str]:
    a_string = ""
    results = []
    for c in s:
        a_string += c
        results.append(a_string)
    return results

print(expansion('test'))
print(expansion(''))
print(expansion('abccba'))