"""
Returns the result of multiplying mat1 by mat2
The dimensions of the input matrices must be valid
https://en.wikipedia.org/wiki/Matrix_multiplication
Examples:
matrix_multiply([[1, 2], [3, 4]], [[1, 2], [3, 4]]) -> [[7, 10], [15, 22]]
matrix_multiply([[1, 2]], [[5], [6]]) -> [[17]]
matrix_multiply([[1], [2]], [[5, 6]]) -> [[5, 10], [6, 12]]
https://matrix.reshish.com/multiplication.php <-- working reference

Note: 
Super famously hard problem (this was my "challenge problem" for my course) Do not try to do LUdecomposition
unless you're feeling very brave XD
"""

def matrix_multiply(mat1 : list[list[int]], mat2 : list[list[int]]) -> list[list[int]]:

    mat1_row = len(mat1)
    mat1_col = len(mat1)
    mat2_row = len(mat2)
    mat2_col = len(mat2)

    


    

def main():
    # print(matrix_multiply([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(matrix_multiply([[1, 2]], [[5], [6]]))
    # print(matrix_multiply([[1], [2]], [[5, 6]]))

if __name__ == "__main__":
    main()