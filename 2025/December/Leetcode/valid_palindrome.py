class Solution:
    def is_palindrome(self, s : str) -> bool:
        s_chars = [c.lower() for c in s if c.isalnum()]
        txt = "".join(s_chars)
        return txt == txt[::-1]

solution = Solution()

test_case_1 = "A man, a plan, a canal: Panama"
test_case_2 = "race a car"
test_case_3 = " "

print(solution.is_palindrome(test_case_1))
print(solution.is_palindrome(test_case_2))
print(solution.is_palindrome(test_case_3))