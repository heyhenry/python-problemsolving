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
def isValid(s : str) -> bool:

    result = True

    stack = []

    for c in s:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        elif len(stack) > 0:
            if c == ')' and '(' == stack[-1]:
                stack.pop()
            elif c == ']' and '[' == stack[-1]:
                stack.pop()
            elif c == '}' and '{' == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)
    
    if len(stack) > 0:
        result = False

    return result

def main():
    print(isValid("()"))
    print(isValid("()[]{}"))
    print(isValid("(]"))
    print(isValid("]"))

if __name__ == "__main__":
    main()