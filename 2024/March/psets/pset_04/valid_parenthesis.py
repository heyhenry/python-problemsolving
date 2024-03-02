"""
1. Valid Parentheses
Your task is to determine if a given collection of parentheses are "valid", meaning that an opening parenthesis
or brace is matched directly with the associated parenthesis or brace.
File format: a single line consisting only of (, [, ), or ]
Output: either true or false
"""
def valid_parenthesis(filename : str) -> bool:

    with open(filename, 'r') as file:

        content = file.read()

        if content:

            stack = []
            last = len(content) - 1
            
            for i in content:
                if i in '([':
                    stack.append(i)
                elif i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()

    return len(stack) == 0
                    
def main():
    print(valid_parenthesis("1/input1.txt"))
    print(valid_parenthesis("1/input2.txt"))
    print(valid_parenthesis("1/input3.txt"))
    print(valid_parenthesis("1/input4.txt"))
    print(valid_parenthesis("1/input5.txt"))

if __name__ == "__main__":
    main()