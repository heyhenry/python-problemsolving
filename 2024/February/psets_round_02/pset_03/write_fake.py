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
from count_words import count_words
from contains import contains

def write_fake(filename : str, words : list[str]):

    with open(filename, 'w') as nfile:

        for w in range(len(words)):
            if w != len(words)-1:
                nfile.write(words[w] + ' ')
            else:
                nfile.write(words[w])

def main():
    # write_fake("files/output.fakeletters", ["test", "out"])
    print(contains("files/output.fakeletters", "test"))
    print(contains("files/output.fakeletters", "other"))
    print(count_words("files/output.fakeletters"))

if __name__ == "__main__":
    main()