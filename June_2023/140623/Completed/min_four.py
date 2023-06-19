"""
Returns the minimum of the four given integers
Examples:
min_four(1, 2, 3, 4) -> 1
min_four(3, 2, 4, 6) -> 2
min_four(0, 0, -5, 0) -> -5
"""

# super simple way
# def min_four(x : int, y : int, z : int, w : int) -> int:
    
#     return min(x, y, z, w)

# abit more work involved
def min_four(x : int, y : int, z : int, w : int) -> int:

    lst = [x, y, z, w]
    min_num = lst[0]

    for i in range(1, len(lst)):
        if lst[i] < min_num:
            min_num = lst[i]

    return min_num

def main():
    print(min_four(1, 2, 3, 4))
    print(min_four(3, 2, 4, 6))
    print(min_four(0, 0, -5, 0))

if __name__ == "__main__":
    main()