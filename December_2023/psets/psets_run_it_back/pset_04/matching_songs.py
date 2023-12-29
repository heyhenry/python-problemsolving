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
                if len(stack) < 1:
                    results.append(row)

            del results[0]
            
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
    
# UPDATE NOTE:
# After reviewing the previous iteration code, problem description. I am confident that my current solution is correct for the given coding problem.
# I believe the issue in regards to why my previous iteration of this problem was able to produce the given solution output is due to overlooking the index counter.
# I believe it does not reset in the case of the character matched against the filter is the same as the previous character.

# Additional analysis using chatgpt noted the following transcript:
# There is a potential issue in the code that might lead to incorrect results. 
# The code compares each character in the song against the corresponding character in the filter, and it increments the index only when a match is found. 
# If there is a character in the song that matches the first character of the filter but does not match the subsequent characters, the index might not be reset, leading to incorrect matches.    