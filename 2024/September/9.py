"""
9. Palindrome Number

Given an integer x, return true if x is a
palindrome, and false otherwise.

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

"""
def is_palindrome(x):

    # solution 1
    # x = str(x)
    # new_x = ''
    # for i in range(len(x)-1, -1, -1):
    #     new_x += x[i]
    # return x == new_x

    # solution 2
    # return str(x) == str(x)[::-1]

    # solution 3
    # x = str(x)
    # return x == x[::-1]

    # solution 4
    number = x
    reverse = 0

    while number > 0:
        last_digit = number % 10
        reverse = reverse * 10 + last_digit
        number = number // 10
        # print(f'Reverse: {reverse}')
        # print(f'Original: {number}')
        # print('---')
    print(f'Reverse: {reverse}')
    print(f'Original: {x}')


def main():
    print(is_palindrome(x = 283))
    print(is_palindrome(x = 121))
    print(is_palindrome(x = -121))
    print(is_palindrome(x = 10))

if __name__ == "__main__":
    main()