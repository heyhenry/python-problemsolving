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

    new_file = 'data_csv/transpose.csv'

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            remove_nl = read_content.splitlines()

            numbers = []
            
            for row in remove_nl:
                line = row.split(',')
                temp = []
                for i in line:
                    temp.append(int(i))
                numbers.append(temp)

            len_list = []

            for row in numbers:
                len_list.append(len(row))
            
            min_row = min(len_list)
            max_row = max(len_list)

            if min_row == max_row:

                results = []

                for col in range(len(numbers[0])):
                    temp = []
                    for row in range(len(numbers)):
                        temp.append(numbers[row][col])
                    results.append(temp)
                
                with open(new_file, 'w') as file:

                    for row in range(len(results)):
                        
                        if row != (len(results) - 1):
                            file.write(str(results[row])+'\n')
                        else:
                            file.write(str(results[row]))
        else:

            with open(new_file, 'w') as file:

                file.write('')
        

def main():
    # print(transpose("data_csv/data1.csv"))
    # print(transpose("data_csv/data2.csv"))
    # print(transpose("data_csv/data3.csv"))
    print(transpose("data_csv/data4.csv"))

if __name__ == "__main__":
    main()