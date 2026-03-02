# Leetcode No.20 Valid Parenthesis
# More Info: https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c not in parenthesis:
                stack.append(c)
            elif stack:
                if stack[-1] == parenthesis[c]:
                    stack.pop()
                else:
                    return False
            else:
                return False

        if len(stack) > 0:
            return False
        return True

s = Solution()

test_case_01 = "()"
test_case_02 = "()[]{}"
test_case_03 = "(]"
test_case_04 = "([])"
test_case_05 = "([)]"
test_case_06 = "(])"

s.isValid(test_case_01)
s.isValid(test_case_02)
s.isValid(test_case_03)
s.isValid(test_case_04)
s.isValid(test_case_05)
s.isValid(test_case_06)