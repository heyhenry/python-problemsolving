"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
def isValid(s: str) -> bool:

    result = True

    if len(s) < 2:
        result = False
    else:
        stack = []

        for c in s:
            if len(stack) > 0:
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)

        result = len(stack) == 0
    
    return result

def main():
    print(isValid("()")) # True
    print(isValid("()[]{}")) # True
    print(isValid("(]")) # False
    print(isValid(")")) # False
    print(isValid("){")) # False
    print(isValid(")[]{}()")) # False

if __name__ == "__main__":
    main()
