"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 
substring without repeating characters.

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

    subs = []
    n = len(s)
    subbie = ''
    result = 0

    for i in range(n):
        if s[i] not in subbie:
            subbie += s[i]
        else:
            subs.append(subbie)
            subbie = subbie[subbie.rfind(s[i])+1:] + s[i]
    
    subs.append(subbie)

    if len(subs) > 0:
        result = len(max(subs, key=len))

    return result

def main():
    print(length_of_longest_substring(s = "abcabcbb"))
    print(length_of_longest_substring(s = "bbbbb"))
    print(length_of_longest_substring(s = "pwwkew"))
    print(length_of_longest_substring(s = "ohvhjdml")) # 6

if __name__ == "__main__":
    main()