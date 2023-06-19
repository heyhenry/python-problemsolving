# Returns the string `s` in reverse order
# Examples:
# reverse_string('abc') -> 'cba'
# reverse_string('') -> ''
# reverse_string('abab') -> 'baba'

def reverse_string(s : str) -> str:

    new_s = ''

    for letter in s:
        new_s = letter + new_s

    return new_s

# What is actually happening with this code / How it's actually reversing the string
# The process below: 
# s = 'abc'
# n = ''
# n = 'a' + '' -> 'a'
# n = 'b' + 'a' -> 'ba'
# n = 'c' + 'ba' -> 'cba'
 
def main():

    print(reverse_string('abc'))
    print(reverse_string(''))
    print(reverse_string('abab'))

if __name__ == "__main__":
    main()