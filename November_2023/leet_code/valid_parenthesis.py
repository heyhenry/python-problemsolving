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
def valid_parenthesis(s : str) -> bool:

    result = True

    p_d = {
        '(':0, 
        ')':0, 
        '[':0, 
        ']':0, 
        '{':0, 
        '}':0
    }

    for c in s:
        if c == '(':
            p_d['('] += 1
        elif c == ')':
            p_d[')'] += 1
        elif c == '[':
            p_d['['] += 1
        elif c == ']':
            p_d[']'] += 1
        elif c == '{':
            p_d['{'] += 1
        elif c == '}':
            p_d['}'] += 1
    
    check_list = []
    
    if p_d['('] == p_d[')']:
        check_list.append(True)
    else:
        check_list.append(False)
    
    if p_d['['] == p_d[']']:
        check_list.append(True)
    else:
        check_list.append(False)

    if p_d['{'] == p_d['}']:
        check_list.append(True)
    else:
        check_list.append(False)

    if False in check_list:
        result = False

    return result

def main():
    print(valid_parenthesis("()"))
    print(valid_parenthesis("()[]{}"))
    print(valid_parenthesis("(]"))

if __name__ == "__main__":
    main()