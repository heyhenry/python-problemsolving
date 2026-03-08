"""
Returns the sum up to each element of the given table
Examples:
row_sum([[1, 2, 3], [4, 5, 6]]) -> [[1, 3, 6], [4, 9, 15]]
row_sum([[], [4], [], [5]]) -> [[], [4], [], [5]]
row_sum([[-1, -5, 6], [7, 2], [10, 10, 10]]) -> [[-1, -6, 0], [7, 9], [10, 20,
30]]
"""
def row_sum(table : list[list[int]]) -> list[list[int]]:
    results = []
    for row in table:
        sum_num = 0
        temp_lst = []
        for i in row:
            sum_num += i
            temp_lst.append(sum_num)
        results.append(temp_lst)
    return results

print(row_sum([[1, 2, 3], [4, 5, 6]]))
print(row_sum([[], [4], [], [5]]))
print(row_sum([[-1, -5, 6], [7, 2], [10, 10, 10]]))