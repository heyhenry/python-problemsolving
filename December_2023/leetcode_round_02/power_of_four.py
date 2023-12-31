"""
342. Power of Four

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

 

Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?
"""
def is_power_of_four(n: int) -> bool:

    result = False

    for i in range(31):
        if n == 4**i:
            result = True

    return result

def main():
    print(is_power_of_four(16))
    print(is_power_of_four(5))
    print(is_power_of_four(1))

if __name__ == "__main__":
    main()