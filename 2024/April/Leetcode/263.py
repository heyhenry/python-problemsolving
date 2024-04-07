def is_ugly(n : int) -> bool:

    while n >= 1:
        if n % 5 == 0:
            n = n // 5
        elif n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        elif n == 1:
            return True
        else:
            return False
        
    return True

def main():
    print(is_ugly(n = 6))
    print(is_ugly(n = 1))
    print(is_ugly(n = 14))

if __name__ == "__main__":
    main()