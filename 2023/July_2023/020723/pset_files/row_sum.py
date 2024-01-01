"""
Returns the sum of each row in the given `.csv` file
Requires that filename ends with `.csv`
Also requires that the given CSV file consist of only integers
Examples:
row_sum("data1.csv") -> []
row_sum("data2.csv") -> [4, 5]
row_sum("data3.csv") -> [2, -4, 18]
row_sum("data4.csv") -> [6, 9, 12, 15]
"""
def row_sum(filename : str) -> list[int]:

    given_extension = filename[-4:]
    desired_extension = '.csv'

    if given_extension == desired_extension:

        with open(filename, 'r') as file:

            read_content = file.read()

            results = []

            if read_content:

                split_lines = read_content.splitlines()

                for row in split_lines:
                    line = row.split(',')
                    sum_value = 0
                    for i in line:
                        sum_value += int(i)
                    results.append(sum_value)

            return results

    else:

        return 'Incorrect file extension provided. Please use .csv.'

def main():
    print(row_sum("data_csv/data1.csv"))
    print(row_sum("data_csv/data2.csv"))
    print(row_sum("data_csv/data4.cssdv"))
    print(row_sum("data_csv/data3.csv"))
    print(row_sum("data_csv/data4.csv"))

if __name__ == "__main__":
    main()