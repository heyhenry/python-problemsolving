"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
def length_of_longest_substring(s : str) -> int:

    n = len(s)
    substr = ''
    stack = []

    for c in s:
        if c not in substr:
            substr += c
        else:
            stack.append(substr)
            substr = substr[substr.rfind(c)+1:] + c

    if substr not in stack:
        stack.append(substr)

    return len(max(stack, key=len))

def main():
    print(length_of_longest_substring(s = "abcabcbb"))
    print(length_of_longest_substring(s = "bbbbb"))
    print(length_of_longest_substring(s = "pwwkew"))
    print(length_of_longest_substring(s = "dvdf"))

if __name__ == "__main__":
    main()