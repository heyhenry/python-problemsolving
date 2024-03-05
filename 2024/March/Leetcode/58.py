"""
58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

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

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""
def length_of_last_word(s : str) -> int:

    # solution 1
    # content = s.split(' ')
    # last_word = ''

    # for i in content[::-1]:
    #     if i.isalpha():
    #         last_word = i
    #         break

    # return len(last_word)

    # solution 2 - signicantly faster than solution 1
    last_word = ''

    for c in s[::-1]:
        if c.isalpha():
            last_word += c
        elif len(last_word) > 0:
            break

    return len(last_word)

def main():
    print(length_of_last_word(s = "Hello World"))
    print(length_of_last_word(s = "   fly me   to   the moon  "))
    print(length_of_last_word(s = "luffy is still joyboy"))

if __name__ == "__main__":
    main()