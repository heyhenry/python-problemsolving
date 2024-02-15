"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

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
def lengthOfLongestSubstring(s : str) -> int:

    subs = []
    substr = ''

    for i in range(len(s)):
        if s[i] not in substr:
            substr += s[i]
        elif s[i] in substr:
            subs.append(substr)
            pos = substr.rfind(s[i])
            substr = substr[pos+1:] + s[i]

    subs.append(substr)

    return len(max(subs, key=len))

def main():
    print(lengthOfLongestSubstring(s = "abcabcbb"))
    print(lengthOfLongestSubstring(s = "bbbbb"))
    print(lengthOfLongestSubstring(s = "pwwkew"))
    print(lengthOfLongestSubstring("dvdf"))



if __name__ == "__main__":
    main()
