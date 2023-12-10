"""
Returns the string `s` in reverse order
Examples:
reverse_string('abc') -> 'cba'
reverse_string('') -> ''
reverse_string('abab') -> 'baba'
"""
def reverse_string(s : str) -> str:

    new_s = ''

    for i in s:
        new_s = i + new_s

    return new_s

def main():
    print(reverse_string('abc'))
    print(reverse_string(''))
    print(reverse_string('abab'))

if __name__ == "__main__":
    main()