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

    if filename[filename.rfind('.')::] == '.fakeletters':

        result = False

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content:

                words = read_content.split(' ')

                for w in words:
                    if w == word:
                        result = True

        return result

def main():
    print(contains("files/test1.fakeletters", "b"))
    print(contains("files/test1.fakeletters", "d"))
    print(contains("files/test2.fakeletters", "wor"))
    print(contains("files/test2.fakeletters", "hello"))
    print(contains("files/test3.fakeletters", ""))

if __name__ == '__main__':
    main()