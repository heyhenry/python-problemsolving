"""
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""
def firstUniqChar(s : str) -> int:

    result = -1

    s_dict = {}

    for c in range(len(s)):
        if s[c] not in s_dict:
            s_dict[s[c]] = 1
        else:
            s_dict[s[c]] += 1

    searcher = ''

    for key, val in s_dict.items():
        if val == 1:
            searcher = key
            break
    
    for c in range(len(s)):
        if s[c] == searcher:
            result = c

    return result
        

def main():
    print(firstUniqChar(s = "leetcode"))
    print(firstUniqChar(s = "loveleetcode"))
    print(firstUniqChar(s = "dddccdbba")) # 8

if __name__ == "__main__":
    main()