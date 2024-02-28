def isPalindrome(s : str) -> bool:

    clean_s = ''

    for c in s:
        if c.isalpha():
            clean_s += c.lower()

    return clean_s == clean_s[::-1]

def main():
    print(isPalindrome(s = "A man, a plan, a canal: Panama"))
    print(isPalindrome(s = "race a car"))
    print(isPalindrome(s = " "))

if __name__ == "__main__":
    main()