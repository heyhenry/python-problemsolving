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
    legend = {'(': ')', '[': ']', '{': '}'}

    for i in range(len(s)):
        if s[i] in legend.keys():
            stack.append(s[i])
        elif stack and s[i] in legend.values():
            if stack[-1] in legend.keys():
                if s[i] in legend[stack[-1]]:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])

    return len(stack) == 0

def main():
    print(is_valid(s = "()"))
    print(is_valid(s = "()[]{}"))
    print(is_valid(s = "(]"))

if __name__ == "__main__":
    main()