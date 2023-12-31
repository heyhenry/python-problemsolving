"""
Returns the maximum even number in `lst`, or `None` if none exists
Note that negatives are even if the associated positive is
Examples:
max_even([1, 2, 3]) -> 2
max_even([-4, 3, -1, -6]) -> -4
max_even([1, 3, 5]) -> None
max_even([0]) -> 0
"""
# solution 1
# def max_even(lst : list[int]) -> int | None:

#     max_even = None

#     for i in lst:
#         if i % 2 == 0:
#             if max_even is None:
#                 max_even = i
#             elif max_even < i:
#                 max_even = i

#     return max_even

# solution 2
# def max_even(lst : list[int]) -> int | None:

#     mnum = None

#     for i in lst:
#         if i % 2 == 0:
#             if mnum is None or mnum < i:
#                 mnum = i

#     return mnum

# solution 2
def max_even(lst : list[int]) -> int | None:

    mnum = 0
    nlist = []

    for i in lst:
        if i % 2 == 0:
            nlist.append(i)

    if len(nlist) > 0:
        mnum = max(nlist)
    else:
        mnum = None

    return mnum

def main():
    print(max_even([1, 2, 3]))
    print(max_even([-4, 3, -1, -6]))
    print(max_even([1, 3, 5]))
    print(max_even([0]))

if __name__ == "__main__":
    main()