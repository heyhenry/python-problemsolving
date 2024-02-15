"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
def longestCommonPrefix(strs : list[str]) -> str:

    result = ''

    if len(strs) == 1:
        result = strs[0]

    else:

        shortest_word = min(strs, key=len)
        
        revised_str = []
        for row in strs:
            s = ''
            for c in range(len(row)):
                if c <= len(shortest_word)-1:
                    s += row[c]
            revised_str.append(s)

        prefix = ''
        prefixes = []

        for col in range(len(revised_str[0])):
            check_cols = []
            for row in range(len(revised_str)):
                check_cols.append(revised_str[row][col])
            if check_cols.count(check_cols[0]) == len(revised_str):
                prefix += check_cols[0]
            else:
                break
        
        prefixes.append(prefix)
        
        if len(prefixes) > 0:
            result = max(prefixes, key=len)

    return result

def main():
    print(longestCommonPrefix(["flower","flow","flight"]))
    print(longestCommonPrefix(["dog","racecar","car"]))
    print(longestCommonPrefix(["a"]))
    print(longestCommonPrefix(["ab", "a"]))

if __name__ == "__main__":
    main()