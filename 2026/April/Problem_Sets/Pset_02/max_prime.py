"""
Returns the maximum prime in the given table, or -1 if none exists
negative numbers, 0, and 1 are not prime numbers
Examples:
max_prime([[1, 4, 8], [0, -5]) -> -1
max_prime([[3, 7, 1, 4], [8, 4, 12, 221]]) -> 7
max_prime([[4, 5, 6], [1, 2, 3], [17, 9, 6]]) -> 17
max_prime([[]]) -> -1
"""
# Reference used for prime validation formula: https://www.programiz.com/python-programming/examples/prime-number

def max_prime(table : list[list[int]]) -> int:
    
    def is_prime(n : int) -> bool:
        if n == 0 or n == 1:
            return False
        elif n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    return False
            return True
        else:
            return False

    max_prime = -1
    for row in table:
        for i in row:
            if is_prime(i):
                if i > max_prime:
                    max_prime = i
    return max_prime

print(max_prime([[1, 4, 8], [0, -5]]))
print(max_prime([[3, 7, 1, 4], [8, 4, 12, 221]]))
print(max_prime([[4, 5, 6], [1, 2, 3], [17, 9, 6]]))
print(max_prime([[]]))