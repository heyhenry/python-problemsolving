"""
Returns the minimum of the four given integers
Examples:
min_four(1, 2, 3, 4) -> 1
min_four(3, 2, 4, 6) -> 2
min_four(0, 0, -5, 0) -> -5
"""
# solution 1 - Using the min function
# def min_four(x : int, y : int, z : int, w : int) -> int:

#     return min(x, y, z, w)

# solution 2 - Using the max function
def min_four(x : int, y : int, z : int, w : int) -> int:

    nums = [x, y, z, w]

    while len(nums) > 1:

        mnum = max(nums)
        nums.remove(mnum)

    return nums[0]

def main():
    print(min_four(1, 2, 3, 4))
    print(min_four(3, 2, 4, 6))
    print(min_four(0, 0, -5, 0))

if __name__ == "__main__":
    main()
