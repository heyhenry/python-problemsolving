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
from contains import contains
from count_words import count_words

def write_fake(filename : str, words : list[str]):

    with open(filename, 'w') as file:

        for i in range(len(words)):
            if i != len(words)-1:
                file.write(words[i] + ' ')
            else:
                file.write(words[i])

def main():
    
    write_fake("fakeletters/output.fakeletters", ["test", "out"])

    print(contains("fakeletters/output.fakeletters", "test")) 
    print(contains("fakeletters/output.fakeletters", "other")) 
    print(count_words("fakeletters/output.fakeletters"))

if __name__ == "__main__":
    main()