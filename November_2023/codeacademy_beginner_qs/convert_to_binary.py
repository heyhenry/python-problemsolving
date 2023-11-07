"""
3. Convert a decimal number into binary
Write a function in Python that accepts a decimal number and returns the equivalent binary number. 
To make this simple, the decimal number will always be less than 1,024, so the binary number returned will always be less than ten digits long.
"""
import math

def convert_to_binary(decimal : float):

    result = []

    while decimal > 1:
        del_num = decimal/2
        rem_num = decimal%2
        decimal -= del_num
        result.append(int(rem_num))
        
    result.reverse()

    return result

def main():
    print(convert_to_binary(520))
    print(convert_to_binary(1022))
    print(convert_to_binary(29))
    print(convert_to_binary(13))

if __name__ == "__main__":
    main()