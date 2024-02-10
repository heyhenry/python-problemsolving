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

    if filename[filename.rfind('.')::] == '.csv':
        
        new_filename = filename[:filename.rfind('.')] + '.transposed'

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content:

                split_lines = read_content.splitlines()
                content = []
                
                for row in split_lines:
                    content.append(row.split(','))

                col_check = True

                for row in content:
                    if len(content[0]) != len(row):
                        col_check = False

                if col_check:
                    
                    transposed_content = []

                    for col in range(len(content[0])):
                        temp = []
                        for row in range(len(content)):
                            temp.append(content[row][col])
                        transposed_content.append(temp)

                    with open(new_filename, 'w') as nfile:

                        for row in range(len(transposed_content)):
                            for i in range(len(transposed_content[row])):
                                if i != len(transposed_content[row]) - 1:
                                    nfile.write(transposed_content[row][i] + ',')
                                else:
                                    nfile.write(transposed_content[row][i])
                            if row != len(transposed_content) - 1:
                                nfile.write('\n')

            else:

                with open(new_filename, 'w') as nfile:

                    nfile.write(' ')


def main():
    print(transpose("files/data1.csv"))
    print(transpose("files/data2.csv"))
    print(transpose("files/data3.csv"))
    print(transpose("files/data4.csv"))

if __name__ == "__main__":
    main()