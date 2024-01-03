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
def firstUniqChar(s: str) -> int:

    result = -1
    char_dict = {}

    counter = -1
    for c in s:
        counter += 1
        if c not in char_dict:
            char_dict[c] = []
            char_dict[c].append(s.count(c))
            char_dict[c].append(counter)
    
    for v in char_dict.values():
        if v[0] == 1:
            result = v[1]
            break

    return result

def main():
    print(firstUniqChar("leetcode"))
    print(firstUniqChar("loveleetcode"))
    print(firstUniqChar("aabb"))

if __name__ == "__main__":
    main()