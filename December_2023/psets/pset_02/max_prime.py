"""
Returns the maximum prime in the given table, or -1 if none exists
negative numbers, 0, and 1 are not prime numbers
Examples:
max_prime([[1, 4, 8], [0, -5]) -> -1
max_prime([[3, 7, 1, 4], [8, 4, 12, 221]]) -> 7
max_prime([[4, 5, 6], [1, 2, 3], [17, 9, 6]]) -> 17
max_prime([[]]) -> -1
"""
def is_prime(n : int):

    result = True

    for i in range(2, n):
        if n % i == 0:
            result = False
    
    return result

def max_prime(table : list[list[int]]) -> int:

    result = None

    for row in table:
        for i in row:
            if is_prime(i):
                if result is None:
                    result = i
                elif i > result:
                    result = i

    if result is None:
        result = -1

    return result

def main():
    print(max_prime([[1, 4, 8], [0, -5]]))
    print(max_prime([[3, 7, 1, 4], [8, 4, 12, 221]]))
    print(max_prime([[4, 5, 6], [1, 2, 3], [17, 9, 6]]))
    print(max_prime([[]]))

if __name__ == "__main__":
    main()