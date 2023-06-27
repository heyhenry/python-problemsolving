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

    extension = filename[-12:]
    if extension == '.fakeletters':

        with open(filename, 'w') as file:

            for w in range(len(words)):
                if w != (len(words) - 1):
                    file.write(words[w])
                    file.write(' ')
                else:
                    file.write(words[w])

    else:
        
        return 'File extension invalid. Please have the (.fakeletters) file name extension to proceed.'

def main():

    # print(write_fake("text_files/output.fakeletters", ["test", "out"]))
    # print(write_fake("text_files/output.wumpus", ["test", "out"]))

    # testing
    print(contains("text_files/output.fakeletters", "test"))
    print(contains("text_files/output.fakeletters", "other"))
    print(count_words("text_files/output.fakeletters"))

if __name__ == "__main__":
    main()