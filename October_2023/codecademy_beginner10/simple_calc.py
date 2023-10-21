"""
7. Create a calculator function
Write a Python function that accepts three parameters. The first parameter is an integer. 
The second is one of the following mathematical operators: +, -, /, or x. The third parameter will also be an integer.

The function should perform a calculation and return the results. For example, if the function is passed 6 and 4, it should return 24.
"""
def calc(num1 : int, num2 : int, operator : str) -> int:

    ans = 0

    if operator == 'x':
        ans = num1 * num2
    elif operator == '+':
        ans = num1 + num2
    elif operator == '-':
        ans = num1 - num2
    elif operator == '/':
        ans = num1 / num2
    else:
        ans = None

    return ans

def main():
    print(calc(5, 5, 'x')) # 25
    print(calc(1, 6, '+')) # 7
    print(calc(10, 3, '-')) # 7
    print(calc(21, 7, '/')) # 3
    print(calc(12, 23, 'o'))

if __name__ == "__main__":
    main()