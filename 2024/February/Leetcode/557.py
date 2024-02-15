"""
557. Reverse Words in a String III

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""
def reverseWords(s : str) -> str:

    words = s.split(' ')
    rev_words = ''

    for w in range(len(words)):
        if w != len(words) - 1:
            rev_words += words[w][::-1] + ' '
        else:
            rev_words += words[w][::-1]

    return rev_words

def main():
    print(reverseWords(s = "Let's take LeetCode contest"))
    print(reverseWords(s = "Mr Ding"))

if __name__ == "__main__":
    main()