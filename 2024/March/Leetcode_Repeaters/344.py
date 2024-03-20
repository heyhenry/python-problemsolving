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
def reverse_string(s : list[str]) -> None:

    s.reverse()

def main():
    s = ["h","e","l","l","o"]
    print(s)
    reverse_string(s)
    print(s)

    t = ["H","a","n","n","a","h"]
    print(t)
    reverse_string(t)
    print(t)

if __name__ == "__main__":
    main()