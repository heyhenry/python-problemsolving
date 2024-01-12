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
def longestCommonPrefix(strs: list[str]) -> str:

    # solution by https://leetcode.com/problems/longest-common-prefix/solutions/3273176/python3-c-java-19-ms-beats-99-91/
    # ans = ''
    # strs = sorted(strs)
    # first = strs[0]
    # last = strs[-1]
    # for i in range(min(len(first),len(last))):
    #     if(first[i]!=last[i]):
    #         return ans
    #     ans+=first[i]
    # return ans

    result = ''

    if len(strs) == 1:
        result = strs[0]
        
    else:
        min_len = min(strs, key=len)
        
        prefixes = []
        
        prefix = ''
        for col in range(len(min_len)):
            temp = ''
            for row in range(len(strs)):
                temp += strs[row][col]
            if temp == temp[0]*len(temp) and len(temp) > 1 and col == len(min_len) - 1:
                prefix += temp[0]
                prefixes.append(prefix)
            elif temp == temp[0]*len(temp) and len(temp) > 1:
                prefix += temp[0]
            else:
                prefixes.append(prefix)
                prefix = ''
        if len(prefixes) < 1:
            result = strs[0]
        else:
            result = max(prefixes, key=len)
        
    return result

def main():
    print(longestCommonPrefix(strs = ["flower","flow","flight"]))
    print(longestCommonPrefix(strs = ["dog","racecar","car"]))
    print(longestCommonPrefix([""]))
    print(longestCommonPrefix(["a"]))

if __name__ == "__main__":
    main()