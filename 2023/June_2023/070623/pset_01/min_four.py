"""
Returns the minimum of the four given integers
Examples:
min_four(1, 2, 3, 4) -> 1
min_four(3, 2, 4, 6) -> 2
min_four(0, 0, -5, 0) -> -5
"""
def min_four(x : int, y : int, z : int, w : int) -> int:

    return min(x, y, z, w)

def main():

    print(min_four(1, 2, 3, 4))
    print(min_four(3, 2, 4, 6))
    print(min_four(0, 0, -5, 0))

if __name__ == "__main__":
    main()


# Completed