"""
Returns the list of each letter of `s` expanded in sequence
Examples:
expansion('test') -> ['t', 'te', 'tes', 'test']
expansion('') -> []
expansion('abccba') -> ['a', 'ab', 'abc', 'abcc', 'abccb', 'abccba']
"""
def expansion(s : str) -> list[str]:

    a_string = ''
    result = []

    for c in s:
        a_string += c
        result.append(a_string)
    
    return result

def main():
    print(expansion('test'))
    print(expansion(''))                                       
    print(expansion('abccba'))

if __name__ == "__main__":
    main()