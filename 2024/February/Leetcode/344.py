"""
344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
"""
def reverseString(s : list[str]) -> None:

    s.reverse()

def main():
    s1 = ["h","e","l","l","o"]
    s2 = ["H","a","n","n","a","h"]
    print(reverseString(s1))
    print(reverseString(s2))

    print(s1)
    print(s2)

if __name__ == "__main__":
    main()