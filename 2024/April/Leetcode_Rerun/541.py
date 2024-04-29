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
def reverse_str(s : str, k : int) -> str:

    s = list(s)
    n = len(s)

    for i in range(0, n, 2*k):
        s[i:i+k] = s[i:i+k][::-1]

    return ''.join(s)

def main():
    print(reverse_str(s = "abcdefg", k = 2))
    print(reverse_str(s = "abcd", k = 2))

if __name__ == "__main__":
    main()