"""
Returns the number of words in a given `.fakeletters` file
A word consists of any number of letters
Requires that `filename` ends with `.fakeletters`
2 / 5
Examples:
count_words("test1.fakeletters") -> 3
count_words("test2.fakeletters") -> 2
count_words("test3.fakeletters") -> 0
count_words("test4.fakeletters") -> 69 (nice!)
"""
import sys

def count_words(filename : str) -> int:

    result = 0

    with open(filename, 'r') as file:
        
        read_content = file.read()
        
        if read_content:
            
            # stores each line of content in a list, using the new line as the separator
            remove_splitlines = read_content.splitlines()
            result_list = []

            # iterate through the list
            for row in remove_splitlines:
                # filter out all elements in each row that is an empty space
                for i in row.split(' '):
                    # store all 'words' into a new list
                    result_list.append(i)
                
            # count quantity of words in the newly curated list of words
            result = len(result_list)

    return result

def main():

    print(count_words(sys.argv[1]))

if __name__ == "__main__":
    main()
