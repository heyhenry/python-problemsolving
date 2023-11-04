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

    desired_ext = '.csv'
    given_ext = filename[-4:]

    if given_ext == desired_ext:
        with open(filename, 'r') as file:
            read_content = file.read()
            results =[]
            if read_content:
                temp = read_content.splitlines()
                contents = []
                for row in temp:
                    t = []
                    for i in row.split(','):
                        t.append(int(i))
                    contents.append(t)

                n_rows = None

                for row in contents:
                    if n_rows is None:
                        n_rows = len(row)
                    elif len(row) > n_rows:
                        n_rows = len(row)

                for row in contents:
                    while len(row) != n_rows:
                        row.append(0)

                for col in range(len(contents[0])):
                    sum_val = 0
                    mean_val = 0
                    for row in range(len(contents)):
                        sum_val += contents[row][col]
                    mean_val += sum_val / len(contents)
                    results.append(mean_val)

        return results

def main():
    print(column_mean("data/data1.csv"))
    print(column_mean("data/data2.csv"))
    print(column_mean("data/data3.csv"))
    print(column_mean("data/data4.csv"))

if __name__ == "__main__":
    main()