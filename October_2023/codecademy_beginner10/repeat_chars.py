"""
10. Repeat the characters
Create a Python function that accepts a string. The function should return a string, with each character in the original string doubled. 
If you send the function “now” as a parameter, it should return “nnooww,” and if you send “123a!”, it should return “112233aa!!”.
"""
def repeat_chars(s : str) -> str:

    result = ''

    for c in s:
        result += c * 2

    return result

def main():
    print(repeat_chars('now'))
    print(repeat_chars('123a!'))

if __name__ == "__main__":
    main()