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
def first_uniq_char(s : str) -> int:

    d = {}

    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = str(i)
        else:
            d[s[i]] = 'invalid'

    for i in d.values():
        if i.isdigit():
            return int(i)
        
    return -1

def main():
    print(first_uniq_char(s = "leetcode"))
    print(first_uniq_char(s = "loveleetcode"))
    print(first_uniq_char(s = "aabb"))

if __name__ == "__main__":
    main()