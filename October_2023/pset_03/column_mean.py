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

    desired_extension = '.csv'
    given_extension = filename[-4:]

    if desired_extension == given_extension:
        
        with open(filename, 'r') as file:
            
            read_content = file.read()

            if read_content:
                
                lines = read_content.splitlines()
                line = []
                result = []
                final_result = []

                for row in lines:
                    line.append(row.split(','))
                
                for row in line:
                    temp = []
                    for i in row:
                        temp.append(int(i))
                    result.append(temp)
                
                max_rows = None

                for row in result:
                    if max_rows is None:
                        max_rows = len(row)
                    elif max_rows < len(row):
                        max_rows = len(row)

                for row in result:
                    while len(row) != max_rows:
                        row.append(0)

                for col in range(len(result[0])):
                    sum_val = 0
                    mean_val = 0
                    for row in range(len(result)):
                        sum_val += result[row][col]
                    mean_val = sum_val / len(result)
                    final_result.append(mean_val)
                
                return final_result

            return []

    return 'Invalid file extension provided.'

def main():
    print(column_mean("data/data1.csv"))
    print(column_mean("data/data2.csv"))
    print(column_mean("data/data3.csv"))
    print(column_mean("data/data4.csv"))

if __name__ == "__main__":
    main()