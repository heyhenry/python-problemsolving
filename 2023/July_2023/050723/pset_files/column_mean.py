"""
Given a CSV filename, calculate the mean of each col in the CSV
Requires that filename end with `.csv` and the file contains only integers
Any empty row element is assumed to be 0
Examples:
col_mean("data1.csv") -> []
col_mean("data2.csv") -> [3, -1, .5, 2]
col_mean("data3.csv") -> [3, 1, 0]
col_mean("data4.csv") -> [2.5, 3.5, 4.5]
"""
def col_mean(filename : str) -> list[float]:

    d_ext = '.csv'
    ext = filename[-4:]

    if ext == d_ext:

        with open(filename, 'r') as file:

            read_content = file.read()

            results = []

            if read_content:

                remove_nl = read_content.splitlines()

                converted = []

                for row in remove_nl:
                    line = row.split(',')
                    temp = []
                    for i in line:
                        temp.append(int(i))
                    converted.append(temp)
                
                largest_row = None

                for row in converted:
                    if largest_row is None:
                        largest_row = len(row)
                    elif len(row) > largest_row:
                        largest_row = len(row)

                for row in converted:
                    while len(row) != largest_row:
                        row.append(0)

                for col in range(len(converted[0])):
                    sum_value = 0
                    mean_value = 0
                    for row in range(len(converted)):
                        sum_value += converted[row][col]
                    mean_value = sum_value / len(converted)
                    results.append(mean_value)

                return results
        
            return results

    return 'Invalid file extension. Use .csv'

def main():
    print(col_mean("data_csv/data1.csv"))
    print(col_mean("data_csv/data2.csv"))
    print(col_mean("data_csv/data3.csv"))
    print(col_mean("data_csv/data4.csv"))
    print(col_mean("data_csv/data5.csv"))

if __name__ == "__main__":
    main()