class Solution:
    def is_valid(self, s : str) -> bool:
        brackets = {"]": "[", "}": "{", ")": "("}
        stack = []

        for c in s:
            if c in "[({":
                stack.append(c)
            elif stack and brackets[c] == stack[-1]:
                stack.pop()
            else:
                return False
        
        if len(stack) > 0:
            return False
        
        return True

solution = Solution()

test_case_1 = "["
test_case_2 = "()[]{}"
test_case_3 = "(]"
test_case_4 = "([])"
test_case_5 = "([)]"

print(solution.is_valid(test_case_1))
print(solution.is_valid(test_case_2))
print(solution.is_valid(test_case_3))
print(solution.is_valid(test_case_4))
print(solution.is_valid(test_case_5))