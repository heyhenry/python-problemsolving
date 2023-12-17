"""
Your task is to determine if a given collection of parentheses are "valid", meaning that an opening parenthesis
or brace is matched directly with the associated parenthesis or brace.
File format: a single line consisting only of (, [, ), or ]
Output: either true or false
"""
import sys

def valid_parenthesis(s : str) -> bool:

    is_valid = True

    # the live stack
    stack = []

    for c in s:

        # checks if the last element of the stack is the other half of the given close bracket
        # if not, add to the stack
        # else, remove the matching open bracket that is in the stack
        if c == ']' and '[' == stack[len(stack)-1]:
            stack.remove('[')
        elif c == ')' and '(' == stack[len(stack)-1]:
            stack.remove('(')
        else:
            stack.append(c)

    if len(stack) > 0:
        is_valid = False

    return is_valid

def main():

    # to open test case files and assess against function
    with open(sys.argv[1], 'r') as file:
        read_content = file.read()
        print(valid_parenthesis(read_content))

if __name__ == "__main__":
    main()