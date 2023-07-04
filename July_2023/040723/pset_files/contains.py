"""
Returns whether the given word appears in a `.fakeletters` file
Requires that `filename` ends with `.fakeletters`
Examples:
contains("test1.fakeletters", "b") -> True
contains("test1.fakeletters", "d") -> False
contains("test2.fakeletters", "wor") -> False
contains("test2.fakeletters", "hello") -> True
contains("test3.fakeletters", "") -> False
"""
from misc_tools import check_fakeletter_extension

def contains(filename : str, word : str) -> bool:

    ext = filename[-12:]

    if check_fakeletter_extension(ext):

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content:

                words = read_content.split(' ')

                if word in words:
                    return True

            return False

    return 'Invalid file extension. Use .fakeletters'

def main():
    print(contains("fakeletters/test1.fakeletters", "b"))
    print(contains("fakeletters/test1.fakeletters", "d"))
    print(contains("fakeletters/test2.fakeletters", "wor"))
    print(contains("fakeletters/test2.fakeletters", "hello"))
    print(contains("fakeletters/test3.fakeletters", ""))

if __name__ == "__main__":
    main()