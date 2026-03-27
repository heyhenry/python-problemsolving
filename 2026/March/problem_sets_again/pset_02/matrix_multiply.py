
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
    mat1_rows = len(mat1)
    mat2_cols = len(max(mat2, key=len))
    
    results = []
 
    for _ in range(mat1_rows):
        temp = []
        for _ in range(mat2_cols):
            temp.append(0)
        results.append(temp)
    
    for i in range(mat1_rows):
        for j in range(mat2_cols):
            for k in range(len(mat1[0])):
                results[i][j] += mat1[i][k] * mat2[k][j]
    
    return results

test_cases = [
    ([[1, 2], [3, 4]], [[1, 2], [3, 4]]),
    ([[1, 2]], [[5], [6]]),
    ([[1], [2]], [[5, 6]])
]

for i in test_cases:
    print(matrix_multiply(i[0], i[1]))