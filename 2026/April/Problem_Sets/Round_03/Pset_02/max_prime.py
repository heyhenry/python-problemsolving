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
    
    def is_prime(n : int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    max_num = -1
    for row in table:
        for i in row:
            if is_prime(i) and i > max_num:
                max_num = i
    return max_num

print(max_prime([[1, 4, 8], [0, -5]]))
print(max_prime([[3, 7, 1, 4], [8, 4, 12, 221]]))
print(max_prime([[4, 5, 6], [1, 2, 3], [17, 9, 6]]))
print(max_prime([[]]))