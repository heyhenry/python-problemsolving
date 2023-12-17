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

            store_lines = read_content.splitlines()
            
            filter = [c for c in store_lines[0]]

            for song in range(1, len(store_lines)):
                stack = []
                for c in store_lines[song].lower():
                    for i in filter:
                        if i == c and c.count(i) > 1:
                            stack = []
                            stack.append(c)
                        elif i == c and c not in stack:
                            stack.append(c)
                if stack == filter:
                    results.append(store_lines[song])

    return results        
                            
def main():
    print(matching_songs(sys.argv[1]))

if __name__ == "__main__":
    main()