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

    results = []
    desired_extension = '.csv'
    given_extension = filename[filename.rfind('.'):]

    if given_extension == desired_extension:
        
        with open(filename, 'r') as file:
            
            read_content = file.read()
            
            if read_content:
                
                lines = read_content.splitlines()
                
                for row in lines:
                    sum_val = 0
                    for i in row.split(','):
                        sum_val += int(i)
                    results.append(sum_val)

    return results

def main():
    print(row_sum("data/data1.csv"))
    print(row_sum("data/data2.csv"))
    print(row_sum("data/data3.csv"))
    print(row_sum("data/data4.csv"))

if __name__ == "__main__":
    main()