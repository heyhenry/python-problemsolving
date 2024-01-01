# Returns the minimum of the four given integers
# Examples:
# min_four(1, 2, 3, 4) -> 1
# min_four(3, 2, 4, 6) -> 2
# min_four(0, 0, -5, 0) -> -5

def min_four(x : int, y : int, z : int, w : int) -> int:

    min_num = x

    if min_num > y: 
        min_num = y
    if min_num > z:
        min_num = z
    if min_num > w:
        min_num = w
    
    return min_num

def main():
    print(min_four(1, 2, 3, 4))
    print(min_four(3, 2, 4, 6))
    print(min_four(0, 0, -5, 0))

if __name__ == "__main__":
    main()