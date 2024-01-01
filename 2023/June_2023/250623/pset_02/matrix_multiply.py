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

    # matrix_a = MxN
    # matrix_b = NxP
    # matrix_c = MxP
    
    mat1_rows = len(mat1)
    mat1_cols = None
    mat2_rows = len(mat2)
    mat2_cols = None

    for row in mat1:
        if mat1_cols is None:
            mat1_cols = len(row)
        elif mat1_cols < len(row):
            mat1_cols = len(row)    

    for row in mat2:
        if mat2_cols is None:
            mat2_cols = len(row)
        elif mat2_cols < len(row):
            mat2_cols = len(row)

    # matrix a => MxN => mat1_rows x mat1_cols
    # print('MxN: ' + str(mat1_rows) + 'x' + str(mat1_cols))
    # matrix b => NxP => mat2_rows x mat2_cols
    # print('NxP: ' + str(mat2_rows) + 'x' + str(mat2_cols))
    # matrix c => MxP => mat1_rows x mat2_cols
    # print('MxP: ' + str(mat1_rows) + 'x' + str(mat2_cols))

    # create empty prefilled list of lists with 0s values as placeholders
    matrix_c = []

    for row in range(mat1_rows):
        temp = []
        for cols in range(mat2_cols):
            temp.append(0)
        matrix_c.append(temp)

    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                matrix_c[i][j] += mat1[i][k] * mat2[k][j]

    return matrix_c

def main():
    print(matrix_multiply([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(matrix_multiply([[1, 2]], [[5], [6]]))
    print(matrix_multiply([[1], [2]], [[5, 6]])) 

if __name__ == "__main__":
    main()

# struggled
# references used:
# https://stackoverflow.com/questions/9671224/split-a-python-list-into-other-sublists-i-e-smaller-lists
# https://www.programiz.com/python-programming/examples/multiply-matrix

# reflection:
# will have to look back on this and understand how the first call works and how to ensure it works dynamically
# really understand how multiply matrixes work, especially logical flow throughout 