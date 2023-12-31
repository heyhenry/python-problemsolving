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
def longest_common_prefix(strs: list[str]) -> str: 

    result = ''

    if len(strs) > 1:

        new_strs = []

        for row in strs:
            while len(row) < len(max(strs)):
                row += '0'
            new_strs.append(row)

        prefix = ''
        total_prefixes = []

        for col in range(len(new_strs[0])):
            letter = ''
            temp = []
            for row in range(len(new_strs)):
                letter = new_strs[row][col]
                temp.append(letter)
            
            if temp.count(letter) == len(new_strs):
                prefix += temp[0]
            if len(prefix) > 0 and prefix not in total_prefixes:
                total_prefixes.append(prefix)
            
                    

        if len(total_prefixes) > 0:
            result = max(total_prefixes)

    else: 
        result = strs[0]

    return result

def main():
    print(longest_common_prefix(["flower","flow","flight"])) # fl
    print(longest_common_prefix(["dog","racecar","car"])) # ''
    print(longest_common_prefix(["a"])) # a
    print(longest_common_prefix(["ab","a"])) # a
    print(longest_common_prefix(["flower","flower","flower","flower"])) # flower
    print(longest_common_prefix(["cir","car"]))

if __name__ == "__main__":
    main()