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
"""
def lcp(strs):

    row_size = len(strs)
    col_size = len(min(strs, key=len))
    result = ''

    for i in range(col_size):
        temp_check = ''
        for j in range(row_size):
            temp_check += strs[j][i]
        if temp_check[0] * row_size == temp_check:
            result += temp_check[0]
        else:
            break
    
    return result


def main():
    print(lcp(strs = ["flower","flow","flight"]))
    print(lcp(strs = ["dog","racecar","car"]))

if __name__ == "__main__":
    main()