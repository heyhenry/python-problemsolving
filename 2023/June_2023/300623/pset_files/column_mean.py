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

    given_extension = filename[-4:]
    desired_extension = '.csv'

    if given_extension == desired_extension:

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content: 

                split_rows = read_content.splitlines()
                
                numbers = []

                for row in split_rows:
                    line = row.split(',')
                    temp = []
                    for i in line:
                        temp.append(int(i))
                    numbers.append(temp)

                largest_row = None

                for row in numbers:
                    if largest_row is None:
                        largest_row = len(row)
                    elif len(row) > largest_row:
                        largest_row = len(row)

                for row in numbers: 
                    
                    while len(row) != largest_row:
                        row.append(0)

                results = []

                for col in range(len(numbers[0])):
                    sum_value = 0
                    col_mean = 0
                    for row in range(len(numbers)):
                        sum_value += numbers[row][col]
                    col_mean = sum_value / len(numbers)
                    results.append(col_mean)
            
                return results

            return []
    else:
        
        return 'Invalid file extension provided. Please ensure file extension is .csv'

def main():
    print(column_mean("data_csv/data1.csv"))
    print(column_mean("data_csv/data2.csv"))
    print(column_mean("data_csv/data3.csv"))
    print(column_mean("data_csv/data4.csv"))

if __name__ == "__main__":
    main()