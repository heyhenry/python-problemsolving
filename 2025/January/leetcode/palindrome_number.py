class Solution:
    def is_palindrome(self, x: int) -> bool:
        # string based solution
        # return str(x) == str(x)[::-1]

        # mathematical based solution
        # store the original x value for later comparison
        original_x = x
        # if the integer is a negative, can conclude it's not a palindrome
        if x < 0:
            return False
        # code logic for reversing an integer below
        reversed_num = 0
        while x != 0:
            # get the tail digit of the current x value
            tail_digit = x % 10
            # shift the current reversed_num values one position to the left
            reversed_num *= 10
            # add the tail_digit to the reversed_num
            reversed_num += tail_digit
            # remove the tail_digit (more accurately, last position in x) from the current x value
            x //= 10
        # return the boolean result of comparing the original x and the reversed x
        return original_x == reversed_num

solution = Solution()
print(solution.is_palindrome(x = 121))
print(solution.is_palindrome(x = -121))
print(solution.is_palindrome(x = 10))