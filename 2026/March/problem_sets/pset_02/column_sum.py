"""
Returns the sum of each column of the _rectangular_ matrix `mat`
(rectangular means each row is the same length)
Examples:
column_sum([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9] # yes, I did it right this
time
column_sum([[], []]) -> [0]
column_sum([[2, 2], [-1, -2], [3, 9]]) -> [4, 9]
"""
def column_sum(mat : list[list[int]]) -> list[int]:
    results = []
    # maximum column size from given lists
    col_size = len(max(mat, key=len))
    for col in range(col_size):
        col_val = 0
        for row in range(len(mat)):
            # safety check - ensure to only run inside logic if valid column
            # note: aware it's unnessary in this situation, but forming consistent habit
            if col < len(mat[row]):
                col_val += mat[row][col]
        results.append(col_val) 

    # for a completely empty list of lists 
    # (to replicate the expected output provideds)
    if not results:
        results.append(0)

    return results

print(column_sum([[1, 2, 3], [4, 5, 6]]))
print(column_sum([[], []]))
print(column_sum([[2, 2], [-1, -2], [3, 9]]))