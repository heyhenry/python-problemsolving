"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""
def isPalindrome(s : str) -> bool:

    result = False
    reverse_s = ''
    alpha_s = ''


    for c in s:
        if c.isalpha():
            reverse_s = c + reverse_s
            alpha_s += c   

    if reverse_s.lower() == alpha_s.lower():
        result = True

    return result

def main():
    print(isPalindrome("race a car")) # False
    print(isPalindrome("A man, a plan, a canal: Panama")) # True
    print(isPalindrome(" ")) # True
    print(isPalindrome("weak")) # False

if __name__ == "__main__":
    main()
