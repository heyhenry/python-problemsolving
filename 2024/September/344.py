"""
344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
def reverse_string(s : list[str]):

    # solution 1
    # create a shallow copy of the s list
    temp_s = s[:]
    # store the s list's length as a variable to reduce calculations required
    size = len(s)

    # loop through the list in reverse indexes
    for i in range(size-1, -1, -1):
        # replace the s list values with the reversed list values
        s[(size-1)-i] = temp_s[i]
    return s

    # # solution 2
    # s[:] = s[::-1]
    # return s

def main():
    print(reverse_string(s = ["h","e","l","l","o"]))
    print(reverse_string(s = ["H","a","n","n","a","h"]))

if __name__ == "__main__":
    main()