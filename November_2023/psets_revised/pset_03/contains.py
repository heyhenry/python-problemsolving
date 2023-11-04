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

    desired_ext = '.fakeletters'
    given_ext = filename[-12:]

    if given_ext == desired_ext:

        with open(filename, 'r') as file:
            read_content = file.read()
            results = False
            if read_content:
                contents = read_content.split(' ')
                for i in contents:
                    if i == word:
                        results = True
        return results

def main():
    print(contains("fakeletters/test1.fakeletters", "b"))
    print(contains("fakeletters/test1.fakeletters", "d"))
    print(contains("fakeletters/test2.fakeletters", "wor"))
    print(contains("fakeletters/test2.fakeletters", "hello"))
    print(contains("fakeletters/test3.fakeletters", ""))

if __name__ == "__main__":
    main()