"""
Returns the minimum of the four given integers
Examples:
min_four(1, 2, 3, 4) -> 1
min_four(3, 2, 4, 6) -> 2
min_four(0, 0, -5, 0) -> -5
"""
# # solution #1
# def min_four(x : int, y : int, z : int, w : int) -> int:

#     return min(x, y, z, w)

# solution #2 (Long-form)
def less_than(x : int, y : int):

    if x < y:
        return True
    
    return False

def min_four(x : int, y : int, z : int, w : int) -> int:

    if less_than(x , y):
        if less_than(x, z):
            if less_than(x, w):
                return x
            else:
                return w
        if less_than(z, w):
            return z
        else:
            return w
    elif less_than(y, z):
        if less_than(y, w):
            return y
        else:
            return w
    elif less_than(z, w):
        return z

    return w

def main():
    print(min_four(1, 2, 3, 4))
    print(min_four(3, 2, 4, 6))
    print(min_four(0, 0, -5, 0))

if __name__ == "__main__":
    main()