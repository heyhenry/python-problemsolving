""""
We have a database of songs, and now we want to find all songs that have the given letters in them in order.
So if we have the letters ac, then we would get "American Pie", but not "Decades".
File format: a request order (any number of lowercase letters in order), followed by an alphabetical list of
names in the song database (which can be any letter, space, or number).
Output: a list of songs in alphabetical order that match the given request order
Note that capitalization doesn't matter, so a matches both A and a
"""
import sys
def matching_songs(filename : str):

    results = []

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            # store each new line as an element into a list
            store_lines = read_content.splitlines()

            # store each element from the first line (it's the comparison key to match songs)
            filter = [c for c in store_lines[0]]

            # loops through each song excluding the filter line (first line)
            for song in range(1, len(store_lines)):
                # a live stack and index to reference the position of the filter element 
                # so I can compare against the characters of each song
                stack = []
                index = 0
                # looping through each character of each song
                for c in store_lines[song].lower():
                    # checks to see if stack is still available and not all elements have been matched
                    # if conditions are met, add to the stack and update the next element position that needs to be matched
                    if index < len(filter) and c == filter[index]:
                        stack.append(c)
                        index += 1
                # checks and validates whether the stack meets the filter requirement after looping through each song
                if stack == filter:
                    # store it in the final results list
                    results.append(store_lines[song])
    
    return results        
                            
def main():
    print(matching_songs(sys.argv[1]))

if __name__ == "__main__":
    main()