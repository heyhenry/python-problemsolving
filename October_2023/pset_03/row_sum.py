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

    desired_extension = '.csv'
    given_extension = filename[-4:]

    if desired_extension == given_extension:
        with open(filename, 'r') as file:
            read_content = file.read()
            if read_content:
                
                lines = read_content.splitlines()
                line = []
                result = []
                
                for row in lines:
                    line.append(row.split(','))
                
                for row in line:
                    sum_val = 0
                    for i in row:
                        new_val = int(i)
                        sum_val += new_val
                    result.append(sum_val) 
                return result

            return []

    return 'Invalid file extension provided.'

def main():
    print(row_sum("data/data1.csv"))
    print(row_sum("data/data2.csv"))
    print(row_sum("data/data3.csv"))
    print(row_sum("data/data4.csv"))

if __name__ == "__main__":
    main()