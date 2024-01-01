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
import sys

def transpose(filename : str):

    # set up new filename
    new_filename = '_transpose.csv'
    index = filename.rfind('.csv')
    new_filename = filename[:index]+new_filename

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            # create appropriate lists
            split_lines = read_content.splitlines()
            content = []
            for row in split_lines:
                content.append(row.split(','))

            # check if rows are equal
            equal_rows = True
            row_check = len(content[0])
            for row in content:
                if len(row) != row_check:
                    equal_rows = False
            
            # transposes content list
            new_content = []
            if equal_rows:
                for col in range(len(content[0])):
                    temp = []
                    for row in range(len(content)):
                        temp.append(content[row][col])
                    new_content.append(temp)
            
                # # create and add transposed results
                with open(new_filename, 'w') as nfile:

                    for row in range(len(new_content)):
                        for i in range(len(new_content[row])):
                            if i != (len(new_content[row]) - 1):
                                nfile.write(new_content[row][i]+',')
                            else:
                                nfile.write(new_content[row][i])
                        if row != (len(new_content)-1):
                            nfile.write('\n')
        else:
            with open(new_filename, 'w') as nfile:

                nfile.write('')
                
def main():
    print(transpose(sys.argv[1]))

if __name__ == "__main__":
    main()