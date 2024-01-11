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

    result = ""

    if len(strs) < 2 and strs[0] == "":

        result = ""

    else:

        min_word = len(min(strs, key=len))
        modified_strs = []
        for word in strs:
            counter = 0
            new_word = ''
            for c in word:
                if counter < min_word:
                    new_word += c
                    counter += 1
            
            modified_strs.append(new_word)

        tha_word = ''
        save_it = []
        for col in range(len(modified_strs[0])):
            temp = ''
            modi_str = ''
            for row in range(len(modified_strs)):
                temp += modified_strs[row][col]
                modi_str = modified_strs[row][col]
            if temp.count(modi_str) == len(modified_strs):
                tha_word += modi_str
            else:
                save_it.append(tha_word)
                tha_word = ''

        if len(save_it) > 1:
            result = max(save_it, key=len)
        else:
            result = tha_word

    return result

def main():
    print(longestCommonPrefix(strs = ["flower","flow","flight"]))
    print(longestCommonPrefix(strs = ["dog","racecar","car"]))
    print(longestCommonPrefix([""]))
    print(longestCommonPrefix(["a"]))

if __name__ == "__main__":
    main()