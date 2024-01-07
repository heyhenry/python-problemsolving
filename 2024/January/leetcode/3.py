"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
def lengthOfLongestSubstring(s: str) -> int:

    # initial for loop style attempt - back burner
    # result = ''
    # max_sub = ''
    # current_sub = ''
    
    # for i in range(len(s)):
        
    #     if s[i] not in current_sub and i == len(s) - 1:
    #         # print('ping1')
    #         current_sub += s[i]
    #         if len(current_sub) > len(max_sub):
    #             max_sub = current_sub
    #     elif s[i] not in current_sub and i < len(s) - 1:
    #         # print('ping2')
    #         current_sub += s[i]
    #     else:
    #         # print('ping3')
    #         if len(current_sub) > len(max_sub):
    #             # print('tripwire1')
    #             max_sub = current_sub
    #             if i < len(s) - 1 and s[i-1] != s[i]:
    #                 # print('tripwire2')
    #                 current_sub = s[i-1] + s[i]
    #             else:
    #                 # print('tripwire3')
    #                 current_sub = s[i]

    # return len(max_sub)

    # # for loop solution style attempt 2nd angle
    # result = ''
    # sub_str = ''
    # subs = []

    # for i in range(len(s)):
    #     # if i is not the final element and i is not already apart of the current sub_str
    #     # then concatenate to sub_str
    #     if i < len(s) - 1 and s[i] not in sub_str:
    #         sub_str += s[i]
    #     # if i does equal the final element and i is not in the current sub_str
    #     # then add the i to the current sub_str and then add the sub_str to subs list
    #     elif i == len(s) - 1 and s[i] not in sub_str:
    #         sub_str += s[i]
    #         subs.append(sub_str)
    #         break
    #     # if i's position not the final element and i's character is already apart of the current sub_str
    #     # then add the current sub_str to the subs list
    #     elif i < len(s) - 1 and s[i] in sub_str:
    #         subs.append(sub_str)
    #         # now check whether the current i value is the same as the next i value
    #         if s[i] == s[i+1]:
    #             # if it is, then just wipe sub_str anew
    #             sub_str = ''
    #             # if above is not the case, then 
    #         elif s[i] != s[i+1] and i+1 == len(s) - 1:
    #             if s[i-1] != s[i]:
    #                 subs.append(s[i-1]+s[i]+s[i+1])
    #                 break
    #             else:
    #                 subs.append(s[i]+s[i+1])
    #                 break
    #         else:
    #             if s[i-1] != s[i]:
    #                 sub_str = s[i-1]+s[i]
    #             else:
    #                 sub_str = s[i]
    #     elif i == len(s) - 1 and s[i] in sub_str:
    #         subs.append(sub_str)

    # if len(s) < 2:
    #     result = s
    # else:
    #     for i in subs:
    #         if result == '' or len(i) > len(result):
    #             result = i
    # print(subs)
    # return len(result)

    # # while loop solution style attempt
    # subs = []
    # counter = 0

    # while counter < len(s):
    #     sub_s = ''
    #     for i in range(counter, len(s)):
    #         if s[counter+i] not in sub_s and counter+i == len(s) - 1:
    #             sub_s += s[counter+i]
    #             subs.append(sub_s)
    #         elif s[counter+i] not in sub_s and counter+i < len(s) - 1:
    #             sub_s += s[counter+i]
    #         else:
    #             subs.append(sub_s)
    #     counter += 1

    # result = ''
    # print(subs)
    # if len(s) < 2:
    #     result = s
    # else:
    #     for i in subs:
    #         if result == '' or len(i) > len(result):
    #             result = i
                
    # print(len(result))

    result = ''
    counter = 0
    decrease_string = []

    while counter < len(s):
       
        de_str = ''

        for i in range(counter, len(s)):
            de_str += s[i]

        decrease_string.append(de_str)
        counter += 1

    distinct_possibilities = []

    for de_str in decrease_string:
        dis_possible = ''
        for i in de_str:
            if i not in dis_possible:
                dis_possible += i
            else:
                distinct_possibilities.append(dis_possible)
                break

    if len(s) < 2:
        result = s
    else:
        for i in distinct_possibilities:
            if result == '' or len(i) > len(result):
                result = i

    return len(result)

def main():
    print(lengthOfLongestSubstring(s = "abcabcbb")) # 3
    print(lengthOfLongestSubstring(s = "bbbbb")) # 1
    print(lengthOfLongestSubstring(s = "pwwkew")) # 3
    print(lengthOfLongestSubstring(s = " ")) # 1
    print(lengthOfLongestSubstring(s = "")) # 0
    print(lengthOfLongestSubstring(s = "c")) # 1
    print(lengthOfLongestSubstring(s = "au")) # 2
    print(lengthOfLongestSubstring(s = "dvdf")) # 3
    print(lengthOfLongestSubstring(s = "aab")) # 2
    print(lengthOfLongestSubstring(s = "ohomm")) # 3
    print(lengthOfLongestSubstring(s = "anviaj")) # 5

if __name__ == "__main__":
    main()