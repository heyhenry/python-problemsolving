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

    # mxn + nxp = mxp

    m = len(mat1)

    p = 0

    for row in mat2:
        if len(row) > p:
            p = len(row)

    mat3 = []
    
    for row in range(m):
        temp = []
        for _ in range(p):
            temp.append(0)
        mat3.append(temp)

    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for x in range(len(mat2)):
                mat3[i][j] += mat1[i][x] * mat2[x][j]
    
    return mat3

def main():
    print(matrix_multiply([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(matrix_multiply([[1, 2]], [[5], [6]]))
    print(matrix_multiply([[1], [2]], [[5, 6]]))

if __name__ == "__main__":
    main()