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
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""
# # solution 1
# def length_of_last_word(s : str) -> int:

    # # removes spaces between words
    # temp = s.split(' ')

    # result = []

    # for i in temp:
    #     if i != '':
    #         # only add elements that are not an empty string
    #         result.append(i)

    # # return the last lenghth of the last element in the result list
    # return len(result[len(result)-1])

def length_of_last_word(s : str) -> int:
    result = []
    word = ''
    
    for c in range(len(s)):
        # checks to see if the next char is a letter or whitespace/space
        if s[c].isalpha():
            # if valid, will concatenate the chars to form words
            word += s[c]
        elif not s[c].isalpha():
            # checks length of word to ensure it isnt just whitespace/space
            if len(word) > 0:
                # adds the verified word to the list of results
                result.append(word)
            word = ''
        # checks if the last character in the string is a whitespace, if not add the final word
        if c == len(s)-1 and s[c].isalpha():
            result.append(word)
    
    # return the last length of the last element in the result list
    return len(result[len(result)-1])

def main():
    print(length_of_last_word("Hello World"))
    print(length_of_last_word("   fly me   to   the moon  "))
    print(length_of_last_word("luffy is still joyboy"))

if __name__ == "__main__":
    main()