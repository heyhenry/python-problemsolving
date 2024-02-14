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

    if filename[filename.rfind('.')::] == '.csv':

        results = []

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content:

                split_lines = read_content.splitlines()

                content = []

                for row in split_lines:
                    content.append(row.split(','))

                for row in content:
                    sum_val = 0
                    for i in row:
                        sum_val += int(i)
                    results.append(sum_val)

    return results

def main():
    print(row_sum("files/data1.csv"))
    print(row_sum("files/data2.csv"))
    print(row_sum("files/data3.csv"))
    print(row_sum("files/data4.csv"))

if __name__ == "__main__":
    main()