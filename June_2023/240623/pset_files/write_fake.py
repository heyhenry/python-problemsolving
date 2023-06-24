"""
Writes the given list of strings to the `.fakeletters` file
Each word must consist of only letters, and will be written
to be all lowercase and space-separated
(Note, you can use the previous two functions to help test this one!)
Requires that `filename` ends with `.fakeletters`
Example:
write_fake("output.fakeletters", ["test", "out"])
contains("output.fakeletters", "test") -> True
contains("output.fakeletters", "other") -> False
count_words("output.fakeletters") -> 2
"""

import os.path

# checks how many words in the file
def count_words(filename : str) -> int:

    result = 0

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            words = read_content.split(" ")

            result = len(words)

    return result

# checks to see if word is in the file
def contains(filename : str, word : str) -> bool:

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            words = read_content.split(" ")

            if word in words:
                return True
    
    return False

def write_fake(filename : str, words : list[str]):

    # save_path = 'text_files/'

    # full_directory = os.path.join(filename + '.fakeletters')

    # full_directory = filename + '.fakeletters'

    if '.fakeletters' in filename:

        with open(filename, 'w') as file:

            for word in range(len(words)):
                if word != (len(words) - 1):
                    file.write(words[word])
                    file.write(" ")
                else:
                    file.write(words[word])

    else:
    
        return 'The file extension name is not valid. Please use .fakeletters'

def main():
    
    # print(write_fake("text_files/output.fakeletters", ["test", "out"]))

    # testing
    # print(write_fake("text_files/output.boop", ["wont", "save"]))
    print(contains("text_files/output.fakeletters", "test"))
    print(contains("text_files/output.fakeletters", "other"))
    print(count_words("text_files/output.fakeletters"))

if __name__ == "__main__":
    main()