"""
Returns the result of multiplying mat1 by mat2
The dimensions of the input matrices must be valid
https://en.wikipedia.org/wiki/Matrix_multiplication
Examples:
matrix_multiply([[1, 2], [3, 4]], [[1, 2], [3, 4]]) -> [[7, 10], [15, 22]]
matrix_multiply([[1, 2]], [[5], [6]]) -> [[17]]
matrix_multiply([[1], [2]], [[5, 6]]) -> [[5, 10], [6, 12]]
https://matrix.reshish.com/multiplication.php <-- working reference
"""
def matrix_multiply(mat1 : list[list[int]], mat2 : list[list[int]]) -> list[list[int]]:

    reordered_list = []

    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                reordered_list.append(mat1[i][k] * mat2[k][j])

    sum_value = 0

    mats = []

    for i in range(0, len(reordered_list), 2):
        value = reordered_list[i:i + 2]
        mats.append(value)

    results = []

    for row in mats:
        sum_value = 0
        for i in row:
            sum_value += i
        results.append(sum_value)

    updated_mat = []

    for i in range(0, len(results), 2):
        value = results[i:i + 2]
        updated_mat.append(value)

    return updated_mat

# matrices a & b
# [1a, 2a]        [1b, 2b]
#             x              
# [3a, 4a]        [3b, 4b]

# First block = (1a x 1b) + (2a x 3b) = 7

def main():
    print(matrix_multiply([[1, 2], [3, 4]], [[1, 2], [3, 4]])) # written to solve this specific one
    print(matrix_multiply([[1, 2]], [[5], [6]])) # somehow works for this too?
    print(matrix_multiply([[1], [2]], [[5, 6]])) # doesnt work out for this

if __name__ == "__main__":
    main()

# struggled
# references used:
# https://stackoverflow.com/questions/9671224/split-a-python-list-into-other-sublists-i-e-smaller-lists
# https://www.programiz.com/python-programming/examples/multiply-matrix

# reflection:
# will have to look back on this and understand how the first call works and how to ensure it works dynamically
# really understand how multiply matrixes work, especially logical flow throughout 