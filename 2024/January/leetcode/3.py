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

    # time limit exceeded on the final test case 
    # distinct_letters = set(s)

    # result = ''
    # ans = []

    # for i in range(len(s)):
    #     temp = []
    #     for j in range(len(s)+1):
    #         twin_plus = False
    #         if len(s[i:j]) > 1:
    #             for k in distinct_letters:
    #                 if s[i:j].count(k) > 1:
    #                     twin_plus = True
    #                     break
    #             if twin_plus == False:
    #                 ans.append(s[i:j])
    #             else:
    #                 twin_plus = False

    # if len(s) < 2:
    #     result = s
    # elif len(distinct_letters) < 2:
    #     result = '1'
    # else:
    #     for i in ans:
    #         if result == '' or len(i) > len(result):
    #             result = i
    
    # return len(result)

    # AI assisted solution that overcomes the final test case's time complexity issue, based on my solution above
    
    # For the sake of learning.. i will note my intepretation of how it works:
    
    # 1. Initial change that seems to contribute to the reduction of time complexity is the storage of 'len(s)' into a variable, 
    # I believe this is more significant when the loop iterations require a high volume of execution of 'len(s)'
    
    # 2. The usage of set() to find the distinct characters in the given string also contributes towards reducing time complexity.
    # This is due to the reduction line required to be executed and read as the built-in function can do it much faster, than a proposed while/for loop

    # 3. The most significant change would be the proper implementation of the sliding window algorithm/technique. 
    # I believe this helped drastically reduce the time complexity, as it eliminated the traditional string concatenation methods and enhancing sorting/weeding out
    # the potential dupes through a strict and intential walk through instead of my previous attempts where I could store all potential results into a list and then 
    # assess further
    n = len(s)
    distinct_letters = set()
    result = 0
    left, right = 0, 0

    while right < n:
        if s[right] not in distinct_letters:
            distinct_letters.add(s[right])
            right += 1
            result = max(result, right - left)
        else:
            distinct_letters.remove(s[left])
            left += 1

    return result

def main():
    # print(lengthOfLongestSubstring(s = "abcabcbb")) # 3
    # print(lengthOfLongestSubstring(s = "bbbbb")) # 1
    print(lengthOfLongestSubstring(s = "pwwkew")) # 3
    # print(lengthOfLongestSubstring(s = " ")) # 1
    # print(lengthOfLongestSubstring(s = "")) # 0
    # print(lengthOfLongestSubstring(s = "c")) # 1
    # print(lengthOfLongestSubstring(s = "au")) # 2
    # print(lengthOfLongestSubstring(s = "dvdf")) # 3
    # print(lengthOfLongestSubstring(s = "aab")) # 2
    # print(lengthOfLongestSubstring(s = "ohomm")) # 3
    print(lengthOfLongestSubstring(s = "anviaj")) # 5

if __name__ == "__main__":
    main()