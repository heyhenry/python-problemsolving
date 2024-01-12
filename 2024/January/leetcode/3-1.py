"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 
substring
 without repeating characters.

 

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
def lengthOfLongestSubstring(s: str) -> int:

    result = ''

    if len(s) < 2:
        result = s
    else:
        substr = ''
        substr_list = []
        for i in range(len(s)):
            if i == len(s) - 1 and s[i] not in substr:
                substr += s[i]
                substr_list.append(substr)
            elif s[i] not in substr:
                substr += s[i]
            else:
                substr_list.append(substr)
                substr = substr[substr.rfind(s[i]):]     

        result = max(substr_list, key=len)

    return result


def main():
    print(lengthOfLongestSubstring("abcabcbb"))
    print(lengthOfLongestSubstring("bbbbb"))
    print(lengthOfLongestSubstring("pwwkew"))
    print(lengthOfLongestSubstring("dvdf"))

if __name__ == "__main__":
    main()