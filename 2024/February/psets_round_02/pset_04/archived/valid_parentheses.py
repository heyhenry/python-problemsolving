"""
1. Valid Parentheses
Your task is to determine if a given collection of parentheses are "valid", meaning that an opening parenthesis
or brace is matched directly with the associated parenthesis or brace.
File format: a single line consisting only of (, [, "1/input1.txt), or ]
Output: either true or false
"""
def is_valid(filename : str) -> bool:

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            stack = []

            for i in read_content:
                if i in '[(':
                    stack.append(i)
                elif len(stack) > 0 and i == ')' and stack[-1] == '(':
                    stack.pop()
                elif len(stack) > 0 and i == ']' and stack[-1] == '[':
                    stack.pop()
            
    return len(stack) == 0

def main():
    print(is_valid("1/input1.txt"))
    print(is_valid("1/input2.txt"))
    print(is_valid("1/input3.txt"))
    print(is_valid("1/input4.txt"))
    print(is_valid("1/input5.txt"))

if __name__ == "__main__":
    main()
          
