"""
Given a CSV filename `example.csv`
If that file is in the form of a matrix (each row has the same length)
Writes the transpose of that file to `example_transpose.csv`
Otherwise, this function does nothing
A matrix transpose "flips" the matrix over the diagonal:
https://en.wikipedia.org/wiki/Transpose
Examples:
transpose("data1.csv") produces an empty file `data1_transpose.csv`
transpose("data2.csv") does nothing
transpose("data3.csv") produces `data3_transpose.csv` with
1,3,5
-1,-2,6
-2,-5,7
transpose("data4.csv") produces `data4_transpose.csv` with
1,2,3,4
2,3,4,5
3,4,5,6
"""
from utilites import check_extension_csv

def transpose(filename : str):

    if check_extension_csv(filename[-4:]):

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content:

                splitlines = read_content.splitlines()
                lines = [] 

                for row in splitlines:
                    line = row.split(',')
                    temp = []
                    for i in line:
                        temp.append(i)
                    lines.append(temp)
                
                check_col_sizes = None
                is_cols_equal = True
                for row in lines:
                    counter = 0
                    for _ in row:
                        counter += 1
                    if check_col_sizes is None:
                        check_col_sizes = counter
                    elif check_col_sizes != counter:
                        is_cols_equal = False

                if is_cols_equal == True:
                
                    updated_content = []

                    for col in range(len(lines[0])):
                        temp = []
                        for row in range(len(lines)):
                            temp.append(lines[row][col])
                        updated_content.append(temp)

                    given_ext = filename[0:10]

                    with open(given_ext + '_tranpose.csv', 'w') as file:

                        for row in updated_content:
                            for i in range(len(row)):
                                if i != len(row) - 1:
                                    file.write(row[i])
                                    file.write(',')
                                else:
                                    file.write(row[i])
                                    file.write('\n')
            else:

                given_ext = filename[0:10]

                with open(given_ext + '_transpose.csv', 'w') as file:

                    file.write('')

    else:

        return 'Incorrect file extension type.'

def main():
    print(transpose("data/data1.csv"))
    print(transpose("data/data2.csv"))
    print(transpose("data/data3.csv"))
    print(transpose("data/data4.csv"))

if __name__ == "__main__":
    main()