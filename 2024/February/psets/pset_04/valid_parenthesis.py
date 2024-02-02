import sys

def valid_parenthesis(filename : str) -> bool:

    result = True

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content: 

            stack = []

            for i in range(len(read_content)):
                if read_content[i] == '[' or read_content[i] == '(':
                    stack.append(read_content[i])
                elif read_content[i] == ']' and '[' == stack[len(stack) - 1]:
                    stack.pop()
                elif read_content[i] == ')' and '(' == stack[len(stack) - 1]:
                    stack.pop() 

            if len(stack) > 0:
                result = False

    return result

def main():
    print(valid_parenthesis('1/input1.txt')) # true
    print(valid_parenthesis('1/input2.txt')) # false
    print(valid_parenthesis('1/input3.txt')) # false
    print(valid_parenthesis('1/input4.txt')) # true
    print(valid_parenthesis('1/input5.txt')) # false

if __name__ == "__main__":
    main()