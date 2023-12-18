"""
1. Valid Parentheses
Your task is to determine if a given collection of parentheses are "valid", meaning that an opening parenthesis
or brace is matched directly with the associated parenthesis or brace.
File format: a single line consisting only of (, [, ), or ]
Output: either true or false
"""
import sys
def valid_parenthesis(filename : str):

    with open(filename, 'r') as file:

        result = True

        read_content = file.read()

        if read_content:

            # a dynamic stack that will update its size/values dependent on matches found iterating through read_content
            stack = []

            for i in range(len(read_content)):
                # if there is already a opening parenthesis that matches the current element in the loop
                # it will remove the opening parenthesis from the stack 
                if read_content[i] == ']' and stack[len(stack)-1] == '[' or read_content[i] == ')' and stack[len(stack)-1] == '(':
                    stack.pop(len(stack)-1)
                # if there is no closed parenthesis that matches the current element in the loop
                # it will add the closed parenthesis to the stack
                else:
                    stack.append(read_content[i])

            # if there any element left in the stack
            # it means that they were not able to properly match with their respective parenthesis
            if len(stack) > 0:
                result = False
                
    return result

def main():
    print(valid_parenthesis(sys.argv[1]))

if __name__ == "__main__":
    main()