"""
5. Hide the credit card number
Write a function in Python that accepts a credit card number. 
It should return a string where all the characters are hidden with an asterisk except the last four. 
For example, if the function gets sent “4444444444444444”, then it should return “4444”.
"""
def hide_cc(cc : int):
    
    result = ''
    
    if len(str(cc)) != 16:
        result = None
    else:
        result = str(cc)[-4:]
    
    return result

def main():
    print(hide_cc(23123))
    print(hide_cc(4444444444444444))

if __name__ == "__main__":
    main()