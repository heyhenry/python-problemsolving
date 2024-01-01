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

    result = ''
    split_list = []
    combined_list = []

    for c in strs:
        split_list.append(list(c))

    prefix = ''
    row_len = None
    for row in split_list:
        while len(row) != len(max(split_list)):
            row.append('0')
    
    for col in range(len(split_list[0])):
        sval = ''
        for row in range(len(split_list)):
            if split_list[row][col] == '0':
                break
            else:
                sval += split_list[row][col]
        combined_list.append(sval)

    another_split = []

    for comb in combined_list:
        another_split.append(list(comb))

    filter_list = []

    for row in another_split:
        counter = 0
        for c in row:
            if c == row[0]:
                counter += 1
        if len(row) == counter and len(row) > 1:
            filter_list.append(row)

    if len(filter_list) > 1:

        for col in range(len(filter_list[0])):
            for row in range(len(filter_list)):
                prefix += filter_list[row][col]
            break

    if len(prefix) > 1:
        result = prefix

    return result

def main():
    print(longest_common_prefix(["flower","flow","flight"]))
    print(longest_common_prefix(["dog","racecar","car"]))

if __name__ == "__main__":
    main()