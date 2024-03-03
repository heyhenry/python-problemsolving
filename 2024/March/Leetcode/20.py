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
def is_valid(s : str) -> bool:

    s = list(s)
    result = False

    if len(s) > 1:

        stack = []

        for c in s:
            if c in '([{':
                stack.append(c)
            elif len(stack) > 0 and c == ')' and stack[-1] == '(':
                stack.pop()
            elif len(stack) > 0 and  c == ']' and stack[-1] == '[':
                stack.pop()
            elif len(stack) > 0 and  c == '}' and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(c)

        result = len(stack) == 0

    return result

def main():
    print(is_valid(s = "()"))
    print(is_valid(s = "()[]{}"))
    print(is_valid(s = "(]"))
    print(is_valid("]"))
    print(is_valid("){"))

if __name__ == "__main__":
    main()