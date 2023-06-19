"""
Returns the string `s` in reverse order
Examples:
reverse_string('abc') -> 'cba'
reverse_string('') -> ''
reverse_string('abab') -> 'baba'
"""
def reverse_string(s : str) -> str:
    result = ''

    for c in s:
        result = c + result

        #  = f + 
        # f = u + f
        # uf = n + uf
        # nuf = nuf (done, nice!)

    return result

def main():
    print(reverse_string('abc'))
    print(reverse_string(''))
    print(reverse_string('abab'))

if __name__ == "__main__":
    main()

# Completed