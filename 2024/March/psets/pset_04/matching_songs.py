"""
4. Matching 

We have a database of songs, and now we want to find all songs that have the given letters in them in order.
So if we have the letters ac, then we would get "American Pie", but not "Decades".
File format: a request order (any number of lowercase letters in order), followed by an alphabetical list of
names in the song database (which can be any letter, space, or number).
Output: a list of songs in alphabetical order that match the given request order
Note that capitalization doesn't matter, so a matches both A and a
"""
def matching_songs(filename : str):

    results = []
    new_filename = filename[:filename.rfind('.')] + '.solution'

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            content = read_content.splitlines()

            for row in content:
                stack = content[0]
                for i in row.lower():
                    if len(stack) > 0 and i == stack[0]:
                        stack = stack.replace(i, '', 1)
                    elif len(stack) > 0 and i in content[0] and i not in stack:
                        if i == content[0][0]:
                            stack = content[0]
                            stack = stack.replace(i, '', 1)
                        else:
                            stack = content[0]
                    elif len(stack) > 0 and i in content[0] and i in stack:
                        stack = content[0]
                if len(stack) == 0:
                    results.append(row)

    return results

def main():
    print(matching_songs("4/input1.txt"))
    print(matching_songs("4/input2.txt"))
    print(matching_songs("4/input3.txt"))

if __name__ == "__main__":
    main()