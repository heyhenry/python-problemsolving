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

    # time limit exceeded on the final test case 
    distinct_letters = set(s)

    result = ''
    ans = []

    for i in range(len(s)):
        temp = []
        for j in range(len(s)+1):
            twin_plus = False
            if len(s[i:j]) > 1:
                for k in distinct_letters:
                    if s[i:j].count(k) > 1:
                        twin_plus = True
                        break
                if twin_plus == False:
                    ans.append(s[i:j])
                else:
                    twin_plus = False

    if len(s) < 2:
        result = s
    elif len(distinct_letters) < 2:
        result = '1'
    else:
        for i in ans:
            if result == '' or len(i) > len(result):
                result = i
    
    return len(result)

def main():
    # print(lengthOfLongestSubstring(s = "abcabcbb")) # 3
    # print(lengthOfLongestSubstring(s = "bbbbb")) # 1
    print(lengthOfLongestSubstring(s = "pwwkew")) # 3
    # print(lengthOfLongestSubstring(s = " ")) # 1
    # print(lengthOfLongestSubstring(s = "")) # 0
    # print(lengthOfLongestSubstring(s = "c")) # 1
    # print(lengthOfLongestSubstring(s = "au")) # 2
    # print(lengthOfLongestSubstring(s = "dvdf")) # 3
    # print(lengthOfLongestSubstring(s = "aab")) # 2
    # print(lengthOfLongestSubstring(s = "ohomm")) # 3
    print(lengthOfLongestSubstring(s = "anviaj")) # 5

if __name__ == "__main__":
    main()