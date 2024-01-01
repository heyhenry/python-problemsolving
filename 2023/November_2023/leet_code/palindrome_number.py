"""
9. Palindrome Number

Given an integer x, return true if x is a 
palindrome
, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

-231 <= x <= 231 - 1
"""
def is_palindrome(x : int) -> bool:

    result = False

    original_x = list(str(x))

    reverse_x = list(str(x))
    reverse_x.reverse()
    
    if original_x == reverse_x:
        result = True

    return result

def main():
    print(is_palindrome(121)) # true
    print(is_palindrome(-121)) # false
    print(is_palindrome(10)) # false

if __name__ == '__main__':
    main()