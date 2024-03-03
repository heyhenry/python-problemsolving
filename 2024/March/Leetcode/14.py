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
def longest_common_prefix(strs : list[str]) -> str:

    prefix = ''
    rnge = len(min(strs, key=len))
    
    for col in range(rnge):
        temp = []
        for row in range(len(strs)):
            temp.append(strs[row][col])
        if temp.count(temp[0]) == len(temp):
            prefix += temp[0]
        else:
            break
    
    return prefix

def main():
    print(longest_common_prefix(strs = ["flower","flow","flight"]))
    print(longest_common_prefix(strs = ["dog","racecar","car"]))

if __name__ == "__main__":
    main()