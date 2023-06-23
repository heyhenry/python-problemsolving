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

    col_list = []

    for row in results:
        value = len(row)
        col_list.append(value)

    if len(results) > 0:

        highest_col_num = col_list[0]

        for i in col_list:
            if i > highest_col_num:
                highest_col_num = i

        for row in results:
            while len(row) != highest_col_num:
                row.append(0)

        end_results = []

        if len(results) > 0:
            for col in range(len(results[0])):
                sum_value = 0
                counter = 0
                mean_value = 0
                for row in range(len(results)):
                    counter += 1
                    sum_value += results[row][col]
                mean_value = sum_value / counter
                end_results.append(mean_value)

        return end_results
    
    return results

def main():
    print(column_mean("csv_files/data1.csv"))
    print(column_mean("csv_files/data2.csv")) 
    print(column_mean("csv_files/data3.csv"))
    print(column_mean("csv_files/data4.csv"))

if __name__ == "__main__":
    main()