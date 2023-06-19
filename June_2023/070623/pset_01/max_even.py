"""
Returns the maximum even number in `lst`, or `None` if none exists
Note that negatives are even if the associated positive is
Examples:
max_even([1, 2, 3]) -> 2
max_even([-4, 3, -1, -6]) -> -4
max_even([1, 3, 5]) -> None
max_even([0]) -> 0
"""
def max_even(lst : list[int]) -> int | None:

    num = None

    for i in lst:
        if i % 2 == 0 and num is None:
            num = i
        if i % 2 == 0 and i > num:
            num = i

    return num

def main():

    print(max_even([1, 2, 3]))
    print(max_even([-4, 3, -1, -6]))
    print(max_even([1, 3, 5]))
    print(max_even([0]))

if __name__ == "__main__":
    main()

# Completed