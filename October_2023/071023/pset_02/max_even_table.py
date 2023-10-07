"""
Returns the maximum even number in each row of `lst`, or `None` if none exists
Note that negatives will be negative when the associated positive is
Examples:
max_even_table([[1, 2, 3]]) -> [2]
max_even([[-4, 3, -1, -6], [1, 3, 5]) -> [-4, None]
max_even_table([[], [1, 4, 6, 2], [-1, -2]]) -> [None, 6, -2]
"""
def max_even_table(lst : list[list[int]]) -> list[int | None]:

    result = []

    for row in lst:
        enum = None
        for i in row:
            if i is not None and i % 2 == 0:
                if enum is None:
                    enum = i
                elif i > enum:
                    enum = i
        result.append(enum)

    return result

def main():

    print(max_even_table([[1, 2, 3]]))
    print(max_even_table([[-4, 3, -1, -6], [1, 3, 5]]))
    print(max_even_table([[], [1, 4, 6, 2], [-1, -2]]))
    print(max_even_table([[None, 1, None], [1, 2, 3], [2, None, 1]]))

if __name__ == "__main__":
    main()