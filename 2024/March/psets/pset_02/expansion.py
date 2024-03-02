"""
Returns the list of each letter of `s` expanded in sequence
Examples:
expansion('test') -> ['t', 'te', 'tes', 'test']
expansion('') -> []
expansion('abccba') -> ['a', 'ab', 'abc', 'abcc', 'abccb', 'abccba']
"""
def expansion(s : str) -> list[str]:

    expander = []
    txt = ''

    for c in s:
        txt += c
        expander.append(txt)

    return expander

def main():
    print(expansion('test'))
    print(expansion(''))
    print(expansion('abccba'))

if __name__ == "__main__":
    main()
