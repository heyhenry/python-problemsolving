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