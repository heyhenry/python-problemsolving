def uneven_column_sum(mat : list[list[int]]) -> list[int]:

    # checks how many elements in each list
    # find the list with the most elements (aka columns)
    largest_col = None

    for row in mat:
        if largest_col is None:
            largest_col = len(row)
        if len(row) > largest_col:
            largest_col = len(row)

    # add 0s to make all lists equal to the largest row
    for row in mat:
        while len(row) != largest_col:
            row.append(0)

    results = []

    # sum up each column and put end values into a list
    for col in range(len(mat[0])):
        sum_value = 0
        for row in range(len(mat)):
            sum_value += mat[row][col]
        results.append(sum_value)

    return results

def main():
    print(uneven_column_sum([[1, 2, 3], [4, 5, 6]]))
    print(uneven_column_sum([[], []]))
    print(uneven_column_sum([[2, 2], [-1, -2], [3, 9]]))
    print(uneven_column_sum([[2, 2], [5], [1, 2, 3]])) # output -> [8, 4, 3]

if __name__ == "__main__":
    main()