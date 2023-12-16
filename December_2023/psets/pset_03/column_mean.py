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
import sys

def column_mean(filename : str) -> list[float]:

    result = []

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            store_lines = read_content.splitlines()

            content = []

            # final list that stores all related elements and excluding the rest i.e. (',')
            for row in store_lines:
                temp = []
                for i in row.split(','):
                    temp.append(i)
                content.append(temp)

            max_row = 0

            # finds the row with the max length
            for row in content:
                if len(row) > max_row:
                    max_row = len(row)

            # adds filler '0' to rows that smaller than max row in length
            for row in content:
                while len(row) < max_row:
                    row.append('0')

            # calculates the mean value of each column of list
            for col in range(len(content[0])):
                sum_value = 0
                for row in range(len(content)):
                    sum_value += int(content[row][col])
                column_mean = sum_value / len(content)
                result.append(column_mean)
            
    return result

def main():
    print(column_mean(sys.argv[1]))

if __name__ == "__main__":
    main()
