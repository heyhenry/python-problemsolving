"""
Returns the maximum prime in the given table, or -1 if none exists
negative numbers, 0, and 1 are not prime numbers
Examples:
max_prime([[1, 4, 8], [0, -5]) -> -1
max_prime([[3, 7, 1, 4], [8, 4, 12, 221]]) -> 7
max_prime([[4, 5, 6], [1, 2, 3], [17, 9, 6]]) -> 17
max_prime([[]]) -> -1
"""
def is_prime(p : int):
    
    is_prime = True

    for i in range(2, p):
        if p % i == 0:
            is_prime = False
    
    return is_prime

def max_prime(table : list[list[int]]) -> int:

    result = -1
    mprime = None

    for row in table:
        for i in row:
            if is_prime(i):
                if mprime is None:
                    mprime = i
                elif i > mprime:
                    mprime = i
    
    if mprime is not None and mprime > 2:
        result = mprime

    return result
        
def main():
    print(max_prime([[1, 4, 8], [0, -5]]))
    print(max_prime([[3, 7, 1, 4], [8, 4, 12, 221]]))
    print(max_prime([[4, 5, 6], [1, 2, 3], [17, 9, 6]]))
    print(max_prime([[]]))

if __name__ == "__main__":
    main()