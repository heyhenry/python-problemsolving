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

    index = sys.argv[1].rfind('.')
    new_filename = sys.argv[1][:index+1] + 'transposed'

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            # store each line as a new list
            store_lines = read_content.splitlines()

            content = []

            # remove all unnessary content i.e. ','
            for row in store_lines:
                temp = []
                for i in row.split(','):
                    temp.append(i)
                content.append(temp)

            # checks to see if all the rows have the same length
            first_row = len(content[0])
            equal_rows = True
            
            for row in content:
                if first_row != len(row):
                    equal_rows = False
            
            # if all the rows have the same length, begin transposing
            if equal_rows:

                with open(new_filename, 'w') as nfile:

                    # transpoing logic and writing to new file
                    for col in range(len(content[0])):
                        for row in range(len(content)):
                            if row != len(content) - 1:
                                nfile.write(content[row][col] + ',')
                            else:
                                nfile.write(content[row][col])
                        nfile.write('\n')

        else:

            # create an empty file if the given file is empty
            with open(new_filename, 'w') as nfile:

                nfile.write('')

def main():
    print(transpose(sys.argv[1]))

if __name__ == "__main__":
    main()