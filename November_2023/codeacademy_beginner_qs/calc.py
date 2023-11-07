"""
7. Create a calculator function
Write a Python function that accepts three parameters. The first parameter is an integer. 
The second is one of the following mathematical operators: +, -, /, or * . The third parameter will also be an integer.

The function should perform a calculation and return the results. For example, if the function is passed 6 and 4, it should return 24.
"""
def calculate(num_one : int, operand : str, num_two : int):

    result = 0

    if operand == '+':
        result = num_one + num_two
    elif operand == '-':
        result = num_one - num_two
    elif operand == '/':
        result = num_one / num_two
    elif operand == '*':
        result = num_one * num_two

    return result

def main():
    print(calculate(2,'+',2))
    print(calculate(10,'-',3))
    print(calculate(20,'/',5))
    print(calculate(5,'*',5))
    print(calculate(3,'sd',2))

if __name__ == "__main__":
    main()