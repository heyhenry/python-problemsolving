"""
Returns the list of each letter of `s` expanded in sequence
Examples:
expansion('test') -> ['t', 'te', 'tes', 'test']
expansion('') -> []
expansion('abccba') -> ['a', 'ab', 'abc', 'abcc', 'abccb', 'abccba']
"""
def expansion(s : str) -> list[str]:
    # solution 1
    # results = []
    # expanding_s = ""
    # for c in s:
    #     expanding_s += c
    #     results.append(expanding_s)
    # return results

    # solution 2
    if len(s) < 2:
        return [s]

    results = [s[0]]
    for c in range(1, len(s)):
        results.append(results[-1]+s[c])
    return results

print(expansion('test'))
print(expansion(''))
print(expansion('abccba'))