"""
58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""
def lolw(s : str) -> int:

    # remove the white spaces and put each word inside the words list
    words = s.split()
    # return the length of the last element in the words list
    return len(words[-1])
    
def main():
    print(lolw(s = "Hello World"))
    print(lolw(s = "   fly me   to   the moon  "))
    print(lolw(s = "luffy is still joyboy"))

if __name__ == "__main__":
    main()