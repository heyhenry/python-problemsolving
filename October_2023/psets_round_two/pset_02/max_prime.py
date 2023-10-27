"""
Returns the maximum prime in the given table, or -1 if none exists
negative numbers, 0, and 1 are not prime numbers
Examples:
max_prime([[1, 4, 8], [0, -5]) -> -1
max_prime([[3, 7, 1, 4], [8, 4, 12, 221]]) -> 7
max_prime([[4, 5, 6], [1, 2, 3], [17, 9, 6]]) -> 17
max_prime([[]]) -> -1
"""
def is_prime(x : int):

    result = False

    for i in range(2, x):
        if x % i == 0:
            result = False
        result = True

    return result

def max_prime(table : list[list[int]]) -> int:

    result = -1

    for row in table:
        for i in row:
            if is_prime(i):
                if result is None or i > result:
                    result = i
    
    return result

def main():
    print(max_prime([[1, 4, 8], [0, -5]]))
    print(max_prime([[3, 7, 1, 4], [8, 4, 12, 221]]))
    print(max_prime([[4, 5, 6], [1, 2, 3], [17, 9, 6]]))
    print(max_prime([[]]))

if __name__ == "__main__":
    main()