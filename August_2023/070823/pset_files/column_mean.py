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
def column_mean(filename : str) -> list[float]:

    ext = filename[-4:]

    if ext == '.csv':

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content:

                splitlines = read_content.splitlines()

                new_arr = []

                for row in splitlines:
                    line = row.split(',')
                    temp = []
                    for i in line:
                        temp.append(int(i))
                    new_arr.append(temp)

                largest_col_size = None

                for row in new_arr:
                    if largest_col_size is None:
                        largest_col_size = len(row)
                    elif len(row) > largest_col_size:
                        largest_col_size = len(row)

                for row in new_arr:
                    while len(row) != largest_col_size:
                        row.append(0)

                results = []

                for col in range(len(new_arr[0])):
                    sum_value = 0
                    mean_value = None
                    for row in range(len(new_arr)):
                        sum_value += int(new_arr[row][col])
                    if mean_value is None:
                        mean_value = sum_value / len(new_arr)
                    elif sum_value / len(new_arr) > mean_value:
                        mean_value = sum_value / len(new_arr)
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