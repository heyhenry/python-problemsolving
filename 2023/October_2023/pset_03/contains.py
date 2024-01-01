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
def contains(filename : str, word : str) -> bool:

    desired_extension = '.fakeletters'
    given_extension = filename[-12:]

    if given_extension == desired_extension:

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content:

                words = read_content.split(' ')

                for i in words:
                    if i == word:
                        return True
                    
                return False

            return False

    return 'Invalid file extension was provided.'

def main():

    print(contains("fakeletters/test1.fakeletters", "b"))
    print(contains("fakeletters/test1.fakeletters", "d"))
    print(contains("fakeletters/test2.fakeletters", "wor"))
    print(contains("fakeletters/test2.fakeletters", "hello"))
    print(contains("fakeletters/test3.fakeletters", ""))

if __name__ == "__main__":
    main()