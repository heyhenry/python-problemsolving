"""
Returns the maximum prime in the given table, or -1 if none exists
negative numbers, 0, and 1 are not prime numbers
Examples:
max_prime([[1, 4, 8], [0, -5]) -> -1
max_prime([[3, 7, 1, 4], [8, 4, 12, 221]]) -> 7
max_prime([[4, 5, 6], [1, 2, 3], [17, 9, 6]]) -> 17
max_prime([[]]) -> -1
"""
def is_prime(n):
    for i in range(2, n):
        if(n % i) == 0:
            # the logic behind this code is that the range will begin with 2 onwards until just before the given number
            # (the reason behind starting at 2, is because we already know it will be divisible by 1 and itself which supports   
            # one of the immutable rules to determine a prime number; that it can only be divisible by 2 factors (1 and itself))
            # if during this process, the given number is divisible by any of the numbers between 2 and n-1
            # then it can be considered to not be a prime number
            return False
        
    return True

def max_prime(table : list[list[int]]) -> int:
    prime_list = []

    for row in table:
        for i in row:
            if is_prime(i):
                prime_list.append(i)

    if prime_list:
        result = max(prime_list)
    else:
        result = -1

    if result <= 1:
        result = -1

    return result          

def main():
    print(max_prime([[1, 4, 8], [0, -5]]))
    print(max_prime([[3, 7, 1, 4], [8, 4, 12, 221]]))
    print(max_prime([[4, 5, 6], [1, 2, 3], [17, 9, 6]]))
    print(max_prime([[]]))

if __name__ == "__main__":
    main()

# Completed