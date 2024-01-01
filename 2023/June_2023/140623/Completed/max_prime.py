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

    for i in range(2, n):
        if (n % i) == 0:
            return False
    
    if n <= 1:
        return False

    return True

def max_prime(table : list[list[int]]) -> int:
    
    max_prime = None

    for row in table:
        for i in row:
            if is_prime(i):
                if max_prime is None:
                    max_prime = i
                elif i > max_prime:
                    max_prime = i
    
    if max_prime is None:
        max_prime = -1

    return max_prime
            
def main():
    print(max_prime([[1, 4, 8], [0, -5]]))
    print(max_prime([[3, 7, 1, 4], [8, 4, 12, 221]]))
    print(max_prime([[4, 5, 6], [1, 2, 3], [17, 9, 6]]))
    print(max_prime([[]]))

if __name__ == "__main__":
    main()