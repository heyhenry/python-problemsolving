"""
69. Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1
"""
def my_sqrt(x : int) -> int:

    is_true = True
    n = x

    while is_true:

        root = 0.5 * (n + (x/n))

        if (abs(root - n) < 1):
            break

        n = root

    return int(root)


def main():
    print(my_sqrt(4)) # 2
    print(my_sqrt(8)) # 2
    print(my_sqrt(16)) # 4

if __name__ == '__main__':
    main()


# NOTE: Had help for this one... diffulty understanding newtons approximation method of finding the square root of a number
# Resource/Help used: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/