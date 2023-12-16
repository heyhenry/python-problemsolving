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
import sys

def row_sum(filename : str) -> list[int]:

    result = []

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            store_lines = read_content.splitlines()

            for row in store_lines:
                sum_value = 0
                for i in row.split(','):
                    sum_value += int(i)
                result.append(sum_value)
        
    return result

def main():
    print(row_sum(sys.argv[1]))

if __name__ == "__main__":
    main()