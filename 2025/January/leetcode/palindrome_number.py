class Solution:
    def is_palindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

solution = Solution()
print(solution.is_palindrome(x = 121))
print(solution.is_palindrome(x = -121))
print(solution.is_palindrome(x = 10))