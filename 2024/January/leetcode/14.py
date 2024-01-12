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

    # My code before ai help 
    # result = ''

    # if len(strs) == 1:
    #     result = strs[0]
        
    # else:
    #     min_len = min(strs, key=len)
        
    #     prefixes = []
        
    #     prefix = ''
    #     for col in range(len(min_len)):
    #         temp = ''
    #         for row in range(len(strs)):
    #             temp += strs[row][col]
    #         if temp == temp[0]*len(temp) and len(temp) > 1 and col == len(min_len) - 1:
    #             prefix += temp[0]
    #             prefixes.append(prefix)
    #         elif temp == temp[0]*len(temp) and len(temp) > 1:
    #             prefix += temp[0]
    #         else:
    #             prefixes.append(prefix)
    #             prefix = ''
    #     if len(prefixes) < 1:
    #         result = strs[0]
    #     else:
    #         result = max(prefixes, key=len)
        
    # return result

    # solution assisted by ai 
    result = ''

    if len(strs) == 1:
        result = strs[0]
        
    else:
        min_len = min(strs, key=len)
        
        prefix = ''
        for col in range(len(min_len)):
            temp = ''
            for row in range(len(strs)):
                temp += strs[row][col]
            if temp == temp[0]*len(temp) and len(temp) > 1:
                prefix += temp[0]
            else:
                break  # Reset the prefix when a mismatch is encountered
        
        result = prefix

    return result


    # Note to self: The reason behind the difficulty in solving the question seems to significantly stem from not properly understanding core components of the problem. 
    # This can be exampled by the loose understanding of what a prefix was... I was just trying to find chars that were in a matching sequence anywhere in the provided words, 
    # but in reality, a prefix is only at the beginning therefore, I did not and was not supposed to find all potentially matchin sequences chars in a word, rather just look at the beginning. 
    # I believe this mistake can also be attributed to spending too much time on the question (i..e long bouts of sitting and contemplating (hrs+) and in states of delirium and tiredness).

    # What can I do better next time?
    # 1. Take breaks when needed (no point in forcing it when you can't think straight anymore)
    # 2. Rely on resources and solutions once a more than ample period has been dedicated to trying to solve the problem 
    # 3. Break down the question and its key parts and clearly understand them individually and slowly link them to each other

def main():
    print(longestCommonPrefix(strs = ["flower","flow","flight"]))
    print(longestCommonPrefix(strs = ["dog","racecar","car"]))
    print(longestCommonPrefix([""]))
    print(longestCommonPrefix(["a"]))

if __name__ == "__main__":
    main()