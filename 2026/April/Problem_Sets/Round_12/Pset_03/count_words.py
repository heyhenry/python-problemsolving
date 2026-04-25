
""" 
Returns the number of words in a given `.fakeletters` file 

A word consists of any number of letters 

Requires that `filename` ends with `.fakeletters`    
Examples: 
    count_words("test1.fakeletters") -> 3 
    count_words("test2.fakeletters") -> 2 
    count_words("test3.fakeletters") -> 0 
    count_words("test4.fakeletters") -> 69
""" 
def count_words(filename : str) -> int: 
    with open(filename, "r") as file:
        content = file.read()
        if not content:
            return 0
        content = content.split(" ")
        return (len(content))

if __name__ == "__main__":
    fakeletters = [
        "test1.fakeletters",
        "test2.fakeletters",
        "test3.fakeletters",
        "test4.fakeletters"
    ]

    for letter in fakeletters:
        print(count_words("fakeletters/"+letter))