"""
4. Matching songs

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

            content = read_content.splitlines()

            filter = [i for i in content[0]]
            
            for row in content:
                stack = [i for i in content[0]]
                for i in row.lower():
                    
                    if len(stack) < 1:
                        break
                    elif i in filter and i == stack[0]:
                        stack.remove(stack[0])
                    elif i in filter and i != stack[0]:
                        stack = [i for i in content[0]]
                        if i == stack[0]:
                            stack.remove(stack[0])
                    print(stack)
                print(len(stack))
                if len(stack) < 1:
                    results.append(row)
            
    return results
            
def main():
    print(matching_songs(sys.argv[1]))

if __name__ == "__main__":
    main()

# Notes:
# Looking back on my previous answer quickly. I got the answer that reflected the output but honestly, 
# it seems the solution I have given here actually makes more sense. 
# It is late right now but I will review why my previous iteration worked and why the given output solutions were as they were
# as they seem incorrect to me now. 