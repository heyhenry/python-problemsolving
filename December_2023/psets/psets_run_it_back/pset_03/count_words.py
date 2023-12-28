"""
Returns the number of words in a given `.fakeletters` file
A word consists of any number of letters
Requires that `filename` ends with `.fakeletters`
2 / 5
Examples:
count_words("test1.fakeletters") -> 3
count_words("test2.fakeletters") -> 2
count_words("test3.fakeletters") -> 0
count_words("test4.fakeletters") -> 69 (nice!)
"""
import sys

def count_words(filename : str) -> int:

    result = 0

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            content = read_content.split(' ')

            result = len(content)

    return result

def main():
    
    print(count_words(sys.argv[1]))

if __name__ == "__main__":
    main()