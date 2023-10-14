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

    if desired_extension == given_extension:
        
        with open(filename, 'r') as file:

            read_content = file.read()

            split_lines = read_content.splitlines()
            lines = []

            for row in split_lines:
                temp = []
                for i in row.split(','):
                    temp.append(int(i))
                lines.append(temp)
            
            transposed_list = []

            for col in range(len(lines[0])):
                temp = []
                for row in range(len(lines)):
                    temp.append(lines[row][col])
                transposed_list.append(temp)

            # strtransposed_list = []
            
            # for row in transposed_list:
            #     temp = []
            #     for i in row:
            #         temp.append(str(i))
            #     strtransposed_list.append(temp)

            # print(strtransposed_list)

            new_filename = filename[:-4] + '_tranposed.csv'
            
            with open(new_filename, 'w') as nfile:

                for row in transposed_list:
                    for i in range(len(row)):
                        if i != (len(row) - 1):
                            nfile.write(str(row[i]) + ',')
                        else:
                            nfile.write(str(row[i]) + '\n')

    return 'Invalid file extension provided.'

def main():
    # print(transpose("data/data1.csv"))
    # print(transpose("data/data2.csv"))
    print(transpose("data/data3.csv"))
    # print(transpose("data/data4.csv"))

if __name__ == "__main__":
    main()