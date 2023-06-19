"""
Returns the maximum even number in `lst`, or `None` if none exists
Note that negatives are even if the associated positive is
Examples:
max_even([1, 2, 3]) -> 2
max_even([-4, 3, -1, -6]) -> -4
max_even([1, 3, 5]) -> None
max_even([0]) -> 0
"""

# initial solution #1
# def max_even(lst : list[int]) -> int | None:

#     max_num = None

#     for i in lst:
#         if i % 2 == 0 and max_num is None:
#             max_num = i
#         if i % 2 == 0 and i > max_num:
#             max_num = i

#     return max_num

# another solution... maybe better? more lines but no repeat of logic to find even numbers
def max_even(lst : list[int]) -> int | None:

    max_num = None

    for i in lst:
        if i % 2 == 0:
            if max_num is None:
                max_num = i
            elif i > max_num:
                max_num = i

    return max_num
    
def main():
    print(max_even([1, 2, 3]))
    print(max_even([-4, 3, -1, -6]))
    print(max_even([1, 3, 5]))
    print(max_even([0]))

if __name__ == "__main__":
    main()