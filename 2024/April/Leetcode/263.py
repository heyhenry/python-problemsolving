"""
263. Ugly Number

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

 

Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
Example 3:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.
 

Constraints:

-231 <= n <= 231 - 1
"""
def is_ugly(n : int) -> bool:

    while n >= 1:
        if n % 5 == 0:
            n = n // 5
        elif n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        elif n == 1:
            return True
        else:
            return False
        
    return True

def main():
    print(is_ugly(n = 6))
    print(is_ugly(n = 1))
    print(is_ugly(n = 14))

if __name__ == "__main__":
    main()