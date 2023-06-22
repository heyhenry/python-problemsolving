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

    results = []

    with open(filename, 'r') as file:

        for row in file:
            temp = []
            number = ''
            line = row.strip('\n')
            for i in line:
                if i != ',':
                    number += i
                elif i == ',':
                    temp.append(int(number))
                    number = ''
            if number != '':
                temp.append(int(number))

            results.append(temp)
            
        end_results = []

        for row in results:
            sum_value = 0
            for i in row:
                sum_value += i
            end_results.append(sum_value)

    return end_results

def main():
    print(row_sum("csv_files/data1.csv")) # []
    print(row_sum("csv_files/data2.csv")) # [4, 5]
    print(row_sum("csv_files/data3.csv")) # [-2, -4, 18]
    print(row_sum("csv_files/data4.csv")) # [6, 9, 12, 15]

if __name__ == "__main__":
    main()