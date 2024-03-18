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

    stack = []
    n = len(s)

    for i in range(n):
        if s[i] in '([{':
            stack.append(s[i])
        elif len(stack) > 0 and s[i] == ')' and stack[-1] == '(':
            stack.pop()
        elif len(stack) > 0 and s[i] == ']' and stack[-1] == '[':
            stack.pop()
        elif len(stack) > 0 and s[i] == '}' and stack[-1] == '{':
            stack.pop()
        else:
            stack.append(s[i])

    return len(stack) == 0

def main():
    print(is_valid(s = "()"))
    print(is_valid(s = "()[]{}"))
    print(is_valid(s = "(]"))
    print(is_valid(']'))

if __name__ == "__main__":
    main()