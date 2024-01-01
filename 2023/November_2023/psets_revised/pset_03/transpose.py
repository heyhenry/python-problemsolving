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

    desired_ext = ".csv"
    given_ext = filename[-4:]

    if given_ext == desired_ext:
        with open(filename, 'r') as file:

            read_contents = file.read()

            relevant_name = filename[5:-4]
            new_filename = "data/transposed_" + relevant_name + ".csv"

            if read_contents:

                contents = read_contents.splitlines()
                revised_contents = []
                
                for row in contents:
                    temp = []
                    for i in row.split(','):
                        temp.append(int(i))
                    revised_contents.append(temp)
                
                n_rows = None
                rows_equal = True

                for row in revised_contents:
                    if n_rows is None:
                        n_rows = len(row)
                    elif len(row) != n_rows:
                        rows_equal = False

                if rows_equal:

                    new_contents = []

                    for col in range(len(revised_contents[0])):
                        temp = []
                        for row in range(len(revised_contents)):
                            temp.append(revised_contents[row][col])
                        new_contents.append(temp)

                    with open(new_filename, 'w') as nfile:

                        for row in new_contents:
                            for i in range(len(row)):
                                if i != len(row) - 1:
                                    nfile.write(str(row[i]) + ',')
                                else:
                                    nfile.write(str(row[i]) + '\n')
            else:
                with open(new_filename, 'w') as nfile:
                    nfile.write('')

def main():
    # print(transpose("data/data1.csv"))
    # print(transpose("data/data2.csv"))
    print(transpose("data/data3.csv"))
    # print(transpose("data/data4.csv"))

if __name__ == "__main__":
    main()