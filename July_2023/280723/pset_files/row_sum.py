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
from utilities import check_extension_csv

def row_sum(filename : str) -> list[int]:

    if check_extension_csv(filename[-4:]):

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content:

                splitlines = read_content.splitlines()

                results = []

                for row in splitlines:
                    line = row.split(',')
                    sum_value = 0
                    for i in line:
                        sum_value += int(i)
                    results.append(sum_value)

                return results

            return []

    return 'Invalid file extension type.'

def main():
    print(row_sum("data/data1.csv"))
    print(row_sum("data/data2.csv"))
    print(row_sum("data/data3.csv"))
    print(row_sum("data/data4.csv"))

if __name__ == "__main__":
    main()