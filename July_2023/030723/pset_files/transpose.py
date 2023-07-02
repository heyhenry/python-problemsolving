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

                results = []

                for row in split_lines:
                    line = row.split(',')
                    temp = []
                    for i in line:
                        temp.append(i)
                    results.append(temp)

                largest_col = None
                equal_cols = True

                for row in results:
                    counter = 0
                    for i in row:
                        counter += 1
                    if largest_col is None:
                        largest_col = counter
                    elif largest_col != counter:
                        equal_cols = False

                if equal_cols:

                    converted = []

                    for col in range(len(results[0])):
                        temp = []
                        for row in range(len(results)):
                            temp.append(results[row][col])
                        converted.append(temp)

                    new_file = filename[:14] + '_transpose.csv'

                    with open(new_file, 'w') as nfile:

                        updated_converted = []
                        
                        for row in converted:
                            temp = []
                            line = ''
                            for i in range(len(row)):
                                if i != (len(row) - 1):
                                    line += row[i] + ','
                                else:
                                    line += row[i]
                            temp.append(line)
                            updated_converted.append(temp)
                
                        for row in updated_converted:
                            for i in row:
                                if i != range(len(updated_converted) - 1):
                                    nfile.write(i)
                                    nfile.write('\n')
                                else:
                                    nfile.write(i)

                return ''
            
            else:

                new_file = filename[:14] + '_transpose.csv'

                with open(new_file, 'w') as nfile:

                    nfile.write('')
    else:

        return 'Invalid file extension. Must use .csv'

def main():
    print(transpose("data_csv/data1.csv"))
    print(transpose("data_csv/data2.csv"))
    print(transpose("data_csv/data3.csv"))
    print(transpose("data_csv/data4.csv"))

if __name__ == "__main__":
    main()