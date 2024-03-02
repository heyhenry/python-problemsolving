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
def contains(filename : str, word : str) -> bool:

    result = False
    desired_extension = '.fakeletters'
    given_extension = filename[filename.rfind('.'):]

    if given_extension == desired_extension:
        with open(filename, 'r') as file:
            read_content = file.read()
            if read_content:
                content = read_content.split(' ')
                for i in content:
                    if i == word:
                        result = True
                        break
    
    return result

def main():
    print(contains("fakeletters/test1.fakeletters", "b"))
    print(contains("fakeletters/test1.fakeletters", "d"))
    print(contains("fakeletters/test2.fakeletters", "wor"))
    print(contains("fakeletters/test2.fakeletters", "hello"))
    print(contains("fakeletters/test3.fakeletters", ""))

if __name__ == "__main__":
    main()