"""
Returns the maximum even number in each row of `lst`, or `None` if none exists
Note that negatives will be negative when the associated positive is
Examples:
max_even_table([[1, 2, 3]]) -> [2]
max_even([[-4, 3, -1, -6], [1, 3, 5]]) -> [-4, None]
max_even_table([[], [1, 4, 6, 2], [-1, -2]]) -> [None, 6, -2]
"""
def max_even_table(lst : list[list[int]]) -> list[int | None]:
    results = []
    for row in lst:
        max_val = None
        for i in row:
            if i % 2 == 0:
                if max_val is None:
                    max_val = i
                elif i > max_val:
                    max_val = i
        results.append(max_val)
    return results

print(max_even_table([[1, 2, 3]]))
print(max_even_table([[-4, 3, -1, -6], [1, 3, 5]]))
print(max_even_table([[], [1, 4, 6, 2], [-1, -2]]))