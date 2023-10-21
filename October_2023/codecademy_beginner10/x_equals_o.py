"""
6. Are the Xs equal to the Os?
Create a Python function that accepts a string. This function should count the number of Xs and the number of Os in the string. It should then return a boolean value of either True or False.

If the count of Xs and Os are equal, then the function should return True. If the count isn’t the same, it should return False. 
If there are no Xs or Os in the string, it should also return True because 0 equals 0. The string can contain any type and number of characters.
"""
def x_equals_o(s : str) -> bool:

    x_counter = 0
    o_counter = 0

    for c in s:
        if c == 'x':
            x_counter += 1
        elif c == 'o': 
            o_counter += 1
    
    return x_counter == o_counter

def main():
    print(x_equals_o('xoxo')) # true
    print(x_equals_o('xdsdsox')) # false
    print(x_equals_o('xdfsdf')) # false
    print(x_equals_o('sdfsdf')) # true


if __name__ == "__main__":
    main()