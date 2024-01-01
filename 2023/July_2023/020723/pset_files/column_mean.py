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

    given_extension = filename[-4:]
    desired_extension = '.csv'

    if given_extension == desired_extension:

        with open(filename, 'r') as file:

            read_content = file.read()

            results = []

            if read_content:

                split_lines = read_content.splitlines()

                converted = []

                for row in split_lines:
                    line = row.split(',')
                    temp = []
                    for i in line:
                        temp.append(int(i))
                    converted.append(temp)

                largest_col = None

                for row in converted:
                    counter = 0
                    for _ in row:
                        counter += 1
                    if largest_col is None:
                        largest_col = counter
                    elif counter > largest_col: 
                        largest_col = counter

                for row in converted:
                    while len(row) != largest_col:
                        row.append(0)

                for col in range(len(converted[0])):
                    sum_value = 0
                    mean_value = 0
                    for row in range(len(converted)):
                        sum_value += converted[row][col]
                    mean_value = sum_value / len(converted)
                    results.append(mean_value)

            return results

    else:

        return 'Incorrect file extension. Please use .csv.'


def main():
    print(column_mean("data_csv/data1.csv"))
    print(column_mean("data_csv/data2.csv"))
    print(column_mean("data_csv/data3.csv"))
    print(column_mean("data_csv/data1.csdfv"))
    print(column_mean("data_csv/data4.csv"))

if __name__ == "__main__":
    main()