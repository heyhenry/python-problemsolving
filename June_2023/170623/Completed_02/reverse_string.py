"""
Returns the string `s` in reverse order
Examples:
reverse_string('abc') -> 'cba'
reverse_string('') -> ''
reverse_string('abab') -> 'baba'
"""
def reverse_string(s : str) -> str:

    word = ''

    for c in s:
        word = c + word

    return word

def main():
    print(reverse_string('abc'))
    print(reverse_string(''))
    print(reverse_string('abab'))

if __name__ == "__main__":
    main()