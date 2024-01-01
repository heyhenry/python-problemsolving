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

    file = open(filename)
    read_content = file.read()

    word_counter = 0

    for i in read_content:
        if i == ' ':
            word_counter += 1
    
    if len(read_content) >= 1:
        word_counter += 1

    return word_counter

def main():
    print(count_words("fake_letters/test1.fakeletters"))
    print(count_words("fake_letters/test2.fakeletters"))
    print(count_words("fake_letters/test3.fakeletters"))
    print(count_words("fake_letters/test4.fakeletters"))
    print(count_words("fake_letters/output.fakeletters"))

if __name__ == "__main__":
    main()