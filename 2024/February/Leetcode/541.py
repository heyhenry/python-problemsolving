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

    # Studied solution by Marlen09 on leetcode
    lst = list(s)

    for i in range(0, len(lst), 2*k):
        lst[i:i+k] = reversed(lst[i:i+k])

    return "".join(lst)

    # studied numerous resources to understand the question better and to see how the above code actually
    # deals with the 1 first conditional ('If there are fewer than k characters left, reverse them all').
    # The code above addresses it but I dont understand how.. it might just be a thing with string slices I dont understand.

    # Solution: I need to learn more about string slicing and its default use cases for different situations.

def main():
    # print(reverseStr(s = "abcdefg", k = 2))
    # print(reverseStr(s = "abcd", k = 2))
    print(reverseStr(s = "abc", k=4))

if __name__ == "__main__":
    main()
