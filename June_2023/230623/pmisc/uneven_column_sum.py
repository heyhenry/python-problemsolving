"""
Returns the sum of each column of the _rectangular_ matrix `mat`
(rectangular means each row is the same length)
Examples:
column_sum([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9] # yes, I did it right this
time
column_sum([[], []]) -> [0]
column_sum([[2, 2], [-1, -2], [3, 9]]) -> [4, 9]
"""
def uneven_column_sum(mat : list[list[int]]) -> list[int]:

    # finds the number of cols in each row and puts them in a list
    col_list = []

    for row in mat:
        value = len(row)
        col_list.append(value)

    # print(col_list)

    # finds the highest number out of the list of column numbers for each row
    highest_col_num = col_list[0]

    for i in col_list:
        if i > highest_col_num:
            highest_col_num = i

    # print(highest_col_num)            

    # checks each row's length and adds 0s to those that are not equal length to the largest row
    for row in mat:
        while len(row) != highest_col_num:
            row.append(0)

    # test to check row lengths
    # for row in updated_mat:
    #     print(len(row))

    # print(updated_mat)

    results = []

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