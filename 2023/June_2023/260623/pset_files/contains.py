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

    extension = filename[-12:]

    if extension == '.fakeletters':

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content:
                words = read_content.split(' ')
                if word in words: 
                    return True
                else:
                    return False
            
            elif read_content == word:
                
                return True

    else:
        
        return 'Woops! Wrong file extension detected. Your file should have the extension (.fakeletters)'

def main():
    print(contains("text_files/test1.fakeletters", "b"))
    print(contains("text_files/test1.fakeletters", "d"))
    print(contains("text_files/test2.fakeletters", "wor"))
    print(contains("text_files/test2.fakeletters", "hello"))
    print(contains("text_files/test3.fakeletters", ""))
    print(contains("text_files/test3.chupp", ""))

if __name__ == "__main__":
    main()