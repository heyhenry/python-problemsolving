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
    
    # n = len(s)
    # r = {}
    # result = -1

    # for c in range(n):
    #     if s[c] not in r:
    #         r[s[c]] = s.count(s[c])

    # remember_dat = ''

    # for key, val in r.items():
    #     if val == 1:
    #         remember_dat = key
    #         break

    # for i in range(n):

    #     if s[i] == remember_dat:
    #         result = i
    #         break

    # return result   

    result = -1
    n = len(s)
    r = {}

    for i in range(n):
        if s[i] not in r:
            r[s[i]] = s.count(s[i])
            if r[s[i]] == 1:
                result = i
                break

    return result

def main():
    print(first_uniq_char(s = "leetcode"))
    print(first_uniq_char(s = "loveleetcode"))
    print(first_uniq_char(s = "aabb"))

if __name__ == "__main__":
    main()