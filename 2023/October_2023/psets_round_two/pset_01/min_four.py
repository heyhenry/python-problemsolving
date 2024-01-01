"""
Returns the minimum of the four given integers
Examples:
min_four(1, 2, 3, 4) -> 1
min_four(3, 2, 4, 6) -> 2
min_four(0, 0, -5, 0) -> -5
"""
def min_four(x : int, y : int, z : int, w : int) -> int:

    result = None

    lst = [x, y, z, w]

    for i in lst:
        if result is None:
            result = i
        elif i <= result:
            result = i
    
    return result

def main():
    print(min_four(1, 2, 3, 4))
    print(min_four(3, 2, 4, 6))
    print(min_four(0, 0, -5, 0))
    print(min_four(1, 20, 23, 1))

if __name__ == "__main__":
    main()