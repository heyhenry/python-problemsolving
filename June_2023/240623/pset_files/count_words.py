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
def count_words(filename : str) -> int:

    result = 0

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            words = read_content.split(" ")

            result = len(words)

    return result

def main():
    print(count_words("text_files/test1.fakeletters"))
    print(count_words("text_files/test2.fakeletters"))
    print(count_words("text_files/test3.fakeletters"))
    print(count_words("text_files/test4.fakeletters"))

if __name__ == "__main__":
    main()