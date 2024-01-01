"""
5. Hide the credit card number
Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. 
For example, if the function gets sent “4444444444444444”, then it should return “4444”.
"""
def hide_digits(digits : int) -> str:

    asteriks = '************'

    return asteriks + str(digits)[-4:]

def main():
    print(hide_digits(4444444444444444))
    print(hide_digits(1234567891012134))
    print(hide_digits(1231231231231911))
    print(hide_digits(6969699696969420))
    print(hide_digits(123123))

if __name__ == "__main__":
    main()