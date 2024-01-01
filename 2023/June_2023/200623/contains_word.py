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

def main():
    print(contains("fake_letters/test1.fakeletters", "b"))
    print(contains("fake_letters/test1.fakeletters", "d"))
    print(contains("fake_letters/test2.fakeletters", "wor"))
    print(contains("fake_letters/test6.fakeletterss", "Never")) # error message in lieu of boolean output
    print(contains("fake_letters/test2.fakeletters", "hello"))
    print(contains("fake_letters/test3.fakeletters", ""))
    print(contains("fake_letters/test5.fakeletter", "")) # error message in lieu of boolean output

if __name__ == "__main__":
    main()