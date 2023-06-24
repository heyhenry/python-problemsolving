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

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            words = read_content.split(" ")

            if word in words:
                return True
    
    return False

def main():
    print(contains("csv_files/test1.fakeletters", "b"))
    print(contains("csv_files/test1.fakeletters", "d"))
    print(contains("csv_files/test2.fakeletters", "wor"))
    print(contains("csv_files/test2.fakeletters", "hello"))
    print(contains("csv_files/test3.fakeletters", ""))

if __name__ == "__main__":
    main()