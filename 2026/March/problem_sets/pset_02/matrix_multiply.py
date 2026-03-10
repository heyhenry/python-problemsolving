
""" 
Returns the result of multiplying mat1 by mat2 
The dimensions of the input matrices must be valid 
https://en.wikipedia.org/wiki/Matrix_multiplication 

Examples: 
    matrix_multiply([[1, 2], [3, 4]], [[1, 2], [3, 4]]) -> [[7, 10], [15, 22]] 
    matrix_multiply([[1, 2]], [[5], [6]]) -> [[17]] 
    matrix_multiply([[1], [2]], [[5, 6]]) -> [[5, 6], [10, 12]] 
    https://matrix.reshish.com/multiplication.php <-- working reference 
"""
def matrix_multiply(mat1 : list[list[int]], mat2 : list[list[int]]) -> list[list[int]]:
    # mat1 prioritises rows, mat2 prioritises cols
    mat1_rows = len(mat1)
    mat1_cols = len(mat1[0])
    mat2_rows = len(mat2)
    mat2_cols = len(mat2[0])

    result = []
    for _ in range(mat1_rows):
        result.append([0]*mat2_cols)

    for i in range(mat1_rows):
        for j in range(mat2_cols):
            for k in range(mat1_cols):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result

test_cases = [
    ([[1, 2], [3, 4]], [[1, 2], [3, 4]]),
    ([[1, 2]], [[5], [6]]),
    ([[1], [2]], [[5, 6]])
]

for i in test_cases:
    print(matrix_multiply(i[0], i[1]))