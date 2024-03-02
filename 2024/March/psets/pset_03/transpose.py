"""
Given a CSV filename `example.csv`
4 / 5
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

    desired_extension = '.csv'
    given_extension = filename[filename.rfind('.'):]
    new_filename = filename[:filename.rfind('.')] + '.transposed'

    if given_extension == desired_extension:

        with open(filename, 'r') as file:
            
            read_content = file.read()
            
            if read_content:

                lines = read_content.splitlines()
                content = []

                for row in lines:
                    content.append(row.split(','))

                is_equal_cols = True

                for row in content:
                    if len(row) != len(content[0]):
                        is_equal_cols = False
                        break
                
                if is_equal_cols:

                    with open(new_filename, 'w') as nfile:

                        for col in range(len(content[0])):
                            for row in range(len(content)):
                                if row != len(content) - 1:
                                    nfile.write(content[row][col] + ',')
                                else:
                                    nfile.write(content[row][col])
                            if col != len(content[0]) - 1:
                                nfile.write('\n')
                            else:
                                nfile.write('')
            
            else:

                with open(new_filename, 'w') as nfile:

                    nfile.write('')
                                


def main():
    print(transpose("data/data1.csv"))
    print(transpose("data/data2.csv"))
    print(transpose("data/data3.csv"))
    print(transpose("data/data4.csv"))

if __name__ == "__main__":
    main()