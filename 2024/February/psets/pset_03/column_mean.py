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

    if filename[filename.rfind('.'):] == '.csv':

        result = []

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content:

                split_lines = read_content.splitlines()

                content = []
                
                for row in split_lines:
                    content.append(row.split(','))

                cols = None

                for row in content:
                    if cols is None or cols < len(row):
                        cols = len(row)

                for row in content:
                    while len(row) < cols:
                        row.append('0')

                for col in range(len(content[0])):
                    sum_value = 0
                    mean_value = 0 
                    for row in range(len(content)):
                        sum_value += int(content[row][col])
                    mean_value = sum_value / len(content)
                    result.append(mean_value)

        return result

def main():
    print(column_mean("data/data1.csv"))
    print(column_mean("data/data2.csv"))
    print(column_mean("data/data3.csv"))
    print(column_mean("data/data4.csv"))

if __name__ == "__main__":
    main()