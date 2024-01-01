"""
Given a CSV filename, calculate the mean of each column in the CSV
Requires that filename end with `.csv` and the file contains only integers
Any empty row element is assumed to be 0
Examples:
column_mean("data1.csv") -> []
column_mean("data2.csv") -> [3, -1, .5, 2]
column_mean("data3.csv") -> [3, 1, 0]
column_mean("data4.csv") -> [2.5, 3.5, 4.5]
"""
from utilities import check_extension_csv

def column_mean(filename : str) -> list[float]:

    if check_extension_csv(filename[-4:]):

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content:

                splitlines = read_content.splitlines()

                int_list = []

                for row in splitlines:
                    line = row.split(',')
                    temp = []
                    for i in line:
                        temp.append(int(i))
                    int_list.append(temp)

                max_col_size = None

                for row in int_list:
                    counter = 0
                    for _ in row:
                        counter += 1
                    if max_col_size is None:
                        max_col_size = counter
                    elif counter > max_col_size:
                        max_col_size = counter

                for row in int_list:
                    while len(row) != max_col_size:
                        row.append(0)

                results = []

                for col in range(len(int_list[0])):
                    sum_value = 0
                    mean_value = 0
                    for row in range(len(int_list)):
                        sum_value += int_list[row][col]
                    mean_value = sum_value / len(int_list)
                    results.append(mean_value)

                return results
            
            return []

    return 'Invalid file extension type.'

def main():
    print(column_mean("data/data1.csv"))
    print(column_mean("data/data2.csv"))
    print(column_mean("data/data3.csv"))
    print(column_mean("data/data4.csv"))

if __name__ == "__main__":
    main()