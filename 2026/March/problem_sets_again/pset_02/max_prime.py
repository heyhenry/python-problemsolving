"""
Returns the maximum prime in the given table, or -1 if none exists
negative numbers, 0, and 1 are not prime numbers
Examples:
max_prime([[1, 4, 8], [0, -5]) -> -1
max_prime([[3, 7, 1, 4], [8, 4, 12, 221]]) -> 7
max_prime([[4, 5, 6], [1, 2, 3], [17, 9, 6]]) -> 17
max_prime([[]]) -> -1
"""

def max_prime(table : list[list[int]]) -> int:

    def is_prime(num : int):
        if num <= 1:
            return False
        else:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
        return True
    
    results = []
    for row in table:
        for i in row:
            if is_prime(i):
                results.append(i)
    if results:
        return max(results)
    return -1

print(max_prime([[1, 4, 8], [0, -5]]))
print(max_prime([[3, 7, 1, 4], [8, 4, 12, 221]]))
print(max_prime([[4, 5, 6], [1, 2, 3], [17, 9, 6]]))
print(max_prime([[]]))