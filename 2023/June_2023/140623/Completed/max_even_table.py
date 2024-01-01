"""
Returns the maximum even number in each row of `lst`, or `None` if none exists
Note that negatives will be negative when the associated positive is
Examples:
max_even_table([[1, 2, 3]]) -> [2]
max_even([[-4, 3, -1, -6], [1, 3, 5]) -> [-4, None]
max_even_table([[], [1, 4, 6, 2], [-1, -2]]) -> [None, 6, -2]
"""
def max_even_table(lst : list[list[int]]) -> list[int | None]:

    results = []

    for row in lst:
        max_num = None
        for i in row:
            if i % 2 == 0:
                if max_num is None:
                    max_num = i
                elif i > max_num: 
                    max_num = i
        results.append(max_num)

    return results

def main():
    print(max_even_table([[1, 2, 3]]))
    print(max_even_table([[-4, 3, -1, -6], [1, 3, 5]]))
    print(max_even_table([[], [1, 4, 6, 2], [-1, -2]]))

if __name__ == "__main__":
    main()
