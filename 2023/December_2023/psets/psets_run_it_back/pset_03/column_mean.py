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

    results = []

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            split_lines = read_content.splitlines()

            content = []

            for i in split_lines:
                content.append(i.split(','))

            # algorithm to find the largest row length then to add fille '0' to uneven rows
            counter = 0
            while counter < (len(content) * 2):
                max_row = 0
                for row in content:
                    if len(row) > max_row:
                        max_row = len(row)
                    if counter > 2:
                        while len(row) < max_row:
                            row.append('0')
                counter += 1

            # colum mean calculation algorithm
            for col in range(len(content[0])):
                sum_value = 0
                for row in range(len(content)):
                    sum_value += int(content[row][col])
                results.append(sum_value/len(content))
    
    return results

def main():

    print(column_mean(sys.argv[1]))

if __name__ == "__main__":
    main()