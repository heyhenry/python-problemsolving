"""
Returns the string `s` in reverse order
Examples:
reverse_string('abc') -> 'cba'
reverse_string('') -> ''
reverse_string('abab') -> 'baba'
"""
def reverse_string(s : str) -> str:

    rand_string = ''

    for c in s:
        rand_string = rand_string + c

    return rand_string

def main():
    print(reverse_string('abc'))
    print(reverse_string(''))
    print(reverse_string('abab'))

if __name__ == "__main__":
    main()