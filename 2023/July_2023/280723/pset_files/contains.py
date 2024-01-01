"""
Returns whether the given word appears in a `.fakeletters` file
Requires that `filename` ends with `.fakeletters`
Examples:
contains("test1.fakeletters", "b") -> True
contains("test1.fakeletters", "d") -> False
contains("test2.fakeletters", "wor") -> False
contains("test2.fakeletters", "hello") -> True
contains("test3.fakeletters", "") -> False
contains("test4.fakeletters") -> 69 (nice!)
"""
from utilities import check_extension_fakeletter

def contains(filename : str, word : str) -> bool:

    if check_extension_fakeletter(filename[-12:]):

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content:

                words = read_content.split(' ')

                for i in words:
                    if i == word:
                        return True
                    
                return False
                
            return False

    return 'Invalid file extension type.'

def main():
    print(contains("fakeletters/test1.fakeletters", "b"))
    print(contains("fakeletters/test1.fakeletters", "d"))
    print(contains("fakeletters/test2.fakeletters", "wor"))
    print(contains("fakeletters/test2.fakeletters", "hello"))
    print(contains("fakeletters/test3.fakeletters", ""))

if __name__ == "__main__":
    main()