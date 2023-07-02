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
def transpose(filename : str):

    given_extension = filename[-4:]
    desired_extension = '.csv'

    if given_extension == desired_extension:

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content:

                split_lines = read_content.splitlines()

                converted = []

                for row in split_lines:
                    line = row.split(',')
                    temp = []
                    for i in line:
                        temp.append(int(i))
                    converted.append(temp)

                is_equal_cols = True
                largest_col = None

                for row in converted:
                    counter = 0
                    for i in row:
                        counter += 1
                    if largest_col is None:
                        largest_col = counter
                    elif counter != largest_col:
                        is_equal_cols = False

                if is_equal_cols:

                    transposed = []

                    for col in range(len(converted[0])):
                        temp = []
                        for row in range(len(converted)):
                            temp.append(converted[row][col])
                        transposed.append(temp)
                    
                    new_file = filename[:14] + '_transpose.csv'

                    with open(new_file, 'w') as nfile:

                        for row in range(len(transposed)):
                            if row != (len(transposed) - 1):

                                nfile.write((str(transposed[row])).strip('[]').replace(' ', ''))
                                nfile.write('\n')
                            else:
                                nfile.write((str(transposed[row])).strip('[]').replace(' ', ''))
            else:

                new_file = filename[:14] + '_transpose.csv'

                with open(new_file, 'w') as nfile:

                    nfile.write('')
    
    else:

        return 'Incorrect file extension. Plase use .csv.'

def main():
    print(transpose("data_csv/data1.csv"))
    print(transpose("data_csv/data2.csv"))
    print(transpose("data_csv/data3.csv"))
    print(transpose("data_csv/data4.csv"))
    print(transpose("data_csv/data4.csdfsv"))

if __name__ == "__main__":
    main()
