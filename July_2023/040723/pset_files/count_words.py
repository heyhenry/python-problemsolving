"""
Returns the number of words in a given `.fakeletters` file
A word consists of any number of letters
Requires that `filename` ends with `.fakeletters`
Examples:
count_words("test1.fakeletters") -> 3
count_words("test2.fakeletters") -> 2
count_words("test3.fakeletters") -> 0
count_words("test4.fakeletters") -> 69 (nice!)
"""
from misc_tools import check_fakeletter_extension

def count_words(filename : str) -> int:

    given_extension = filename[-12:]

    if check_fakeletter_extension(given_extension):

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content:

                words = read_content.split(' ')

                return len(words)
            
            return 0

    return 'Invalid file extension. Use .fakeletters'


def main():
    print(count_words("fakeletters/test1.fakeletters"))
    print(count_words("fakeletters/test2.fakeletters"))
    print(count_words("fakeletters/test3.fakeletters"))
    print(count_words("fakeletters/test4.fakeletters"))
    print(count_words("fakeletters/test4.wakafla"))

if __name__ == "__main__":
    main()