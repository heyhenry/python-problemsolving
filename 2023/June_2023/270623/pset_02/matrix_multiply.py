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
    mat2_rows = len(mat2)
    mat1_cols = None
    mat2_cols = None

    # calculate the column lengths for mat1 & mat2
    for row in mat1:
        if mat1_cols is None:
            mat1_cols = len(row)
        elif len(row) > mat1_cols:
            mat1_cols = len(row)

    for row in mat2:
        if mat2_cols is None:
            mat2_cols = len(row)
        elif len(row) > mat2_cols:
            mat2_cols = len(row)

    # mxn + nxp = mxp
    # mat1[row][col] + mat2[row][col] = mat3[mat1[row]mat2[col]]

    # create the empty but accurate mat3
    mat3 = []

    for row in range(mat1_rows):
        temp = []
        for _ in range(mat2_cols):
            temp.append(0)
        mat3.append(temp)

    # multiplying mat1 by mat2
    for i in range(len(mat1)): # row
        for j in range(len(mat2[0])): # col
            for k in range(len(mat2)): # len of col
                mat3[i][j] += mat1[i][k] * mat2[k][j]

    return mat3

def main():
    print(matrix_multiply([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(matrix_multiply([[1, 2]], [[5], [6]]))
    print(matrix_multiply([[1], [2]], [[5, 6]]))

if __name__ == "__main__":
    main()