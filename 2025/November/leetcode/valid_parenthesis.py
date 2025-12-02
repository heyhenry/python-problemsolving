class Solution:
    def is_valid(self, s : str) -> bool:
        stack = []
        brackets = {'[': ']', '{': '}', '(': ')'}
        for c in s:
            if c in "[({":
                stack.append(c)
            elif stack:
                if brackets[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0
        
solution = Solution()

test_case_1 = "()"
test_case_2 = "()[]{}"
test_case_3 = "(]"
test_case_4 = "([])"
test_case_5 = "(])"

print(solution.is_valid(test_case_1)) # true
print(solution.is_valid(test_case_2)) # true
print(solution.is_valid(test_case_3)) # false
print(solution.is_valid(test_case_4)) # true
print(solution.is_valid(test_case_5)) # false