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
    desired_extension = '.csv'
    given_extension = filename[filename.rfind('.'):]

    with open(filename, 'r') as file:
        
        read_content = file.read() 
        
        if read_content:
            
            lines = read_content.splitlines()
            content = []
            
            for row in lines:
                content.append(row.split(','))
            
            max_col_len = len(max(content, key=len))
            
            for row in content:
                while len(row) < max_col_len:
                    row.append(str(0))

            for col in range(len(content[0])):
                sum_val = 0
                mean_val = 0
                for row in range(len(content)):
                    sum_val += int(content[row][col])
                mean_val = sum_val / len(content)
                results.append(mean_val)
    
    return results

def main():
    print(column_mean("data/data1.csv"))
    print(column_mean("data/data2.csv"))
    print(column_mean("data/data3.csv"))
    print(column_mean("data/data4.csv"))

if __name__ == "__main__":
    main()