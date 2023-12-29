"""
1. Valid Parentheses

Your task is to determine if a given collection of parentheses are "valid", meaning that an opening parenthesis
or brace is matched directly with the associated parenthesis or brace.
File format: a single line consisting only of (, [, ), or ]
Output: either true or false
"""
import sys

def valid_parenthesis(s : str): 

    result = True
    stack = []

    for c in range(len(s)):
        if s[c] == '[':
            stack.append(s[c])
        elif s[c] == '(':
            stack.append(s[c])
        elif (s[c] == ']' and stack[len(stack)-1] == '['):
            stack.remove('[')
        elif (s[c] == ')' and stack[len(stack)-1] == '('):
            stack.remove('(')
        
    if len(stack) > 0:
        result = False
        
    return result

def main():

    with open(sys.argv[1], 'r') as file:

        read_content = file.read()

        print(valid_parenthesis(read_content))

if __name__ == "__main__":
    main()