"""
541. Reverse String II

Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"
 

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 104
"""
def reverseStr(s : str, k : int) -> str:

    if len(s) < k:
        return s[::-1]
    elif len(s) < 2*k and k >= len(s):
        temp = ''
        for c in range(2):
            temp += c
        temp = temp[::-1]
        for c in range(2, len(s)):
            temp += c
        return temp


    # else:
    #     pairs_lst = []
    #     counter = 0
    #     temp = []
    #     for c in s:
    #         counter += 1
    #         temp.append(c)
    #         if counter == 2:
    #             pairs_lst.append(temp)
    #             counter = 0
    #             temp = []
        
    #     equal_lengths = True

    #     for pair in pairs_lst:
    #         if len(pair) != len(pairs_lst[0]):
    #             equal_lengths = False

    
        
    # print(pairs_lst)

def main():
    # print(reverseStr(s = "abcdefg", k = 2))
    # print(reverseStr(s = "abcd", k = 2))
    print(reverseStr(s = "abcdefghi", k = 3))

if __name__ == "__main__":
    main()
