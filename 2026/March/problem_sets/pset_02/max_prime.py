"""
Returns the maximum prime in the given table, or -1 if none exists
negative numbers, 0, and 1 are not prime numbers
Examples:
max_prime([[1, 4, 8], [0, -5]) -> -1
max_prime([[3, 7, 1, 4], [8, 4, 12, 221]]) -> 7
max_prime([[4, 5, 6], [1, 2, 3], [17, 9, 6]]) -> 17
max_prime([[]]) -> -1
"""
# Reference used for prime validation formula: https://www.geeksforgeeks.org/python/python-program-to-check-whether-a-number-is-prime-or-not/

def max_prime(table : list[list[int]]) -> int:
    # left this function within max_prime, due to scenario not requiring outside reusability
    def is_prime(num : int):
        if num <= 1:
            return False
        else:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
        return True

    result = -1
    for row in table:
        for i in row:
            if is_prime(i):
                if i > result:
                    result = i
    return result

print(max_prime([[1, 4, 8], [0, -5]]))
print(max_prime([[3, 7, 1, 4], [8, 4, 12, 221]]))
print(max_prime([[4, 5, 6], [1, 2, 3], [17, 9, 6]]))
print(max_prime([[]]))