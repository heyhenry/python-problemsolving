"""
231. Power of Two

Companies
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?
"""
def is_power_of_two(n: int) -> bool:

    got_em = False

    for i in range(31):
        if n == 2**i:
            got_em = True

    return got_em

def main():
    print(is_power_of_two(1))
    print(is_power_of_two(16))
    print(is_power_of_two(3))

if __name__ == "__main__":
    main()