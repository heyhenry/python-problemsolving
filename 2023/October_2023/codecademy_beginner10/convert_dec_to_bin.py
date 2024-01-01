"""
3. Convert a decimal number into binary
Write a function in Python that accepts a decimal number and returns the equivalent binary number. 
To make this simple, the decimal number will always be less than 1,024, so the binary number returned will always be less than ten digits long.
"""
def convert_to_binary(decimal : int) -> int:

    take_num = 0
    result = ''

    while decimal >= 1:
        result += str(int(decimal % 2))
        take_num = decimal / 2
        decimal -= take_num

    return result

def main():
    print(convert_to_binary(13))
    print(convert_to_binary(1024))
    print(convert_to_binary(223))
    print(convert_to_binary(313))

if __name__ == "__main__":
    main()

