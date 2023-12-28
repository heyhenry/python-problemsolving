"""
Returns the list of each letter of `s` expanded in sequence
Examples:
expansion('test') -> ['t', 'te', 'tes', 'test']
expansion('') -> []
expansion('abccba') -> ['a', 'ab', 'abc', 'abcc', 'abccb', 'abccba']
"""
def expansion(s : str) -> list[str]:

    results = []
    new_s = ''

    for c in s:
        new_s += c
        results.append(new_s)

    return results

def main():
    print(expansion('test'))
    print(expansion(''))
    print(expansion('abccba'))

if __name__ == "__main__":
    main()
