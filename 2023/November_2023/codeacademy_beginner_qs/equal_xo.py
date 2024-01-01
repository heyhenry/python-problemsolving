"""
6. Are the Xs equal to the Os?
Create a Python function that accepts a string. This function should count the number of Xs and the number of Os in the string. 
It should then return a boolean value of either True or False.

If the count of Xs and Os are equal, then the function should return True. If the count isn’t the same, it should return False. 
If there are no Xs or Os in the string, it should also return True because 0 equals 0. 
The string can contain any type and number of characters.
"""
def equal_xo(s : str):

    result = True
    x_count = s.count('x')
    o_count = s.count('o')
    
    if x_count != o_count:
        result = False

    return result

def main():
    print(equal_xo('xoxo'))
    print(equal_xo('xxooox'))
    print(equal_xo('xoxxo'))
    print(equal_xo('xx'))
    print(equal_xo('watermeln'))

if __name__ == "__main__":
    main()