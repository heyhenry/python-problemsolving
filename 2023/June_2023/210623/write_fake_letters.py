import os.path
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
def write_fake(filename : str, words : list[str]):

    directory = "fake_letters"
    file = open(os.path.join(directory, filename), 'w')

    for word in words:
        if word == words[-1]:
            file.write(word)
        else:
            file.write(word)
            file.write(' ')


def contains(filename : str, word : str) -> bool:

    desired_extension = 'fakeletters'

    file = open(filename)

    extension = filename.split('.')[1]

    if extension == desired_extension:

        read_content = file.read()

        words = []
        a_word = ''

        for i in read_content:
            
            if i != ' ':
                a_word += i
            else:
                words.append(a_word)
                a_word = ''
        
        if len(a_word) > 0:
            words.append(a_word)

        for w in words:
            if w == word:
                return True
            
        return False
    
    return "Wrong file extension. Please provide a file with the ('fakeletters') extension type"

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

    # To create a fake letter
    # print(write_fake("output.fakeletters", ["test", "out"]))

    # For testing
    print(contains("fake_letters/output.fakeletters", "test")) 
    print(contains("fake_letters/output.fakeletters", "other")) 
    print(count_words("fake_letters/output.fakeletters")) 

if __name__ == "__main__":
    main()