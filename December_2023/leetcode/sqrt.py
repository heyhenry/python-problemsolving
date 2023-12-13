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

    result = 0

    # last num smaller than x
    x_minus = 0

    for i in range(1, x):
        if i * i == x:
            result = i

        # finds and stores the last number that is smaller than x
        if i * i < x:
            x_minus = i

    # if the for loop is unable to find an appropriate square root num, then assume it was overshot as the loop only iterates whole numbers.
    # this means that the answer is a float number that is more than x_minus but less than the given x
    # since we round down as per the given guidelines, this suffices in finding the square root of given x
    if result == 0:
        result = x_minus

    return result


def main():
    # perfect squares
    print(my_sqrt(4)) # 2
    print(my_sqrt(8)) # 2

    # non-perfect squares
    print(my_sqrt(2)) # 1
    print(my_sqrt(10)) # 3
    print(my_sqrt(15)) # 3
    print(my_sqrt(20)) # 4

    # bigger nums
    # perfect square
    print(my_sqrt(144)) #12
    # non-perfect square
    print(my_sqrt(123)) # 11 
    print(my_sqrt(987)) # 31

if __name__ == "__main__":
    main()