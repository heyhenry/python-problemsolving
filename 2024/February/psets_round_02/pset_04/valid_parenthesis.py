"""
1. Valid Parentheses
Your task is to determine if a given collection of parentheses are "valid", meaning that an opening parenthesis
or brace is matched directly with the associated parenthesis or brace.
File format: a single line consisting only of (, [, ), or ]
Output: either true or false
"""
def is_valid(filename : str) -> bool:

    result = True

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            stack = []

            for c in range(len(read_content)):
                if read_content[c] in '[(':
                    stack.append(read_content[c])
                elif len(stack) > 0 and read_content[c] == ')' and stack[-1] == '(':
                    stack.pop()
                elif len(stack) > 0 and read_content[c] == ']' and stack[-1] == '[':
                    stack.pop()
                
            if len(stack) > 0:
                result = False

    return result

def main():
    print(is_valid("1/input1.txt"))
    print(is_valid("1/input2.txt"))
    print(is_valid("1/input3.txt"))
    print(is_valid("1/input4.txt"))
    print(is_valid("1/input5.txt"))

if __name__ == "__main__":
    main()