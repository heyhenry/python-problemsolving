# Returns the maximum prime in the given table, or -1 if none exists
# negative numbers, 0, and 1 are not prime numbers
# Examples:
# max_prime([[1, 4, 8], [0, -5]) -> -1
# max_prime([[3, 7, 1, 4], [8, 4, 12, 221]]) -> 7
# max_prime([[4, 5, 6], [1, 2, 3], [17, 9, 6]]) -> 17
# max_prime([[]]) -> -1

def is_prime(n):
    for i in range(2, n):
        if(n%i) == 0:
            return False
    return True

def max_prime(table : list[list[int]]) -> int:

    max_prime_num = -1

    for row in table:
        for num in row:
            if is_prime(num) and num > 0 and num != 1:
                if max_prime_num == -1:
                    max_prime_num = num
                else:
                    if max_prime_num < num:
                        max_prime_num = num

    return max_prime_num

def main():

    print(max_prime([[1, 4, 8], [0, -5]]))
    print(max_prime([[3, 7, 1, 4], [8, 4, 12, 221]]))
    print(max_prime([[4, 5, 6], [1, 2, 3], [17, 9, 6]]))
    print(max_prime([[]]))
    print(max_prime([[8, 5]]))
    print(max_prime([[5, 9]]))

if __name__ == "__main__":

    main()