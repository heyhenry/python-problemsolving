"""
Returns the sum of each row in the given `.csv` file
Requires that filename ends with `.csv`
Also requires that the given CSV file consist of only integers
Examples:
row_sum("data1.csv") -> []
row_sum("data2.csv") -> [4]
row_sum("data3.csv") -> [2, -4, 18]
row_sum("data4.csv") -> [6, 9, 12, 15]
"""
def row_sum(filename : str) -> list[int]:

    with open(filename, 'r') as file:
        
        read_content = file.read()

        numbers = read_content.splitlines()

        results = []

        for row in numbers:
            line = row.split(',')
            sum_value = 0
            for i in line:
                sum_value += int(i)
            results.append(sum_value)

    return results

def main():
    print(row_sum("csv_files/data1.csv"))
    print(row_sum("csv_files/data2.csv"))
    print(row_sum("csv_files/data3.csv"))
    print(row_sum("csv_files/data4.csv"))

if __name__ == "__main__":
    main()