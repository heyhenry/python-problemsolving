"""
4. Matching songs
We have a database of songs, and now we want to find all songs that have the given letters in them in order.
So if we have the letters ac, then we would get "American Pie", but not "Decades".
File format: a request order (any number of lowercase letters in order), followed by an alphabetical list of
names in the song database (which can be any letter, space, or number).
Output: a list of songs in alphabetical order that match the given request order
Note that capitalization doesn't matter, so a matches both A and a
"""
def matches_found(filename : str) -> list[str]:

    results = []

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            songs = read_content.splitlines()

            filtered_stack = [x for x in songs[0]]
            filtered_stack_copy = []

            for song in range(1, len(songs)):
                filtered_stack_copy += filtered_stack
                for c in songs[song].lower():
                    if len(filtered_stack_copy) > 0 and c == filtered_stack_copy[0]:
                        filtered_stack_copy.pop(0)
                    elif len(filtered_stack_copy) > 0 and c in filtered_stack:
                        filtered_stack_copy.clear()
                        filtered_stack_copy += filtered_stack
                        if c == filtered_stack_copy[0]:
                            filtered_stack_copy.pop(0)
                if len(filtered_stack_copy) == 0:
                    results.append(songs[song])
                filtered_stack_copy.clear()

    return results

def main():
    print(matches_found("4/input1.txt"))
    print(matches_found("4/input2.txt"))
    print(matches_found("4/input3.txt"))

if __name__ == "__main__":
    main()