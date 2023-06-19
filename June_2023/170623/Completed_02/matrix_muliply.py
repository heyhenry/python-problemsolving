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

    results = []

    # for i in range(len(mat1)):
    #     for j in range(len(mat2)):
    #         # print(mat2[j], mat1[i])
    #         # results =
    #         # 5 1
    #         # 5 2
    #         # 6 1
    #         # 6 2

def main():
    print(matrix_multiply([[1, 2]], [[5], [6]]))

if __name__ == "__main__":
    main()