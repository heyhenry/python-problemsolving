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
def is_prime(i : int) -> bool:

    result = True

    for n in range(2, i):
        if i % n == 0:
            return False

    return result

def is_ugly(n : int) -> bool:

    result = False

    nums = [2, 3, 5]

    if n == 1:
        result = True
    else:
        for i in nums:
            for j in nums:
                if i * j == n:
                    result = True

    return result

def main():
    print(is_ugly(6))
    print(is_ugly(1))
    print(is_ugly(14))
    print(is_ugly(2))

if __name__ == "__main__":
    main()