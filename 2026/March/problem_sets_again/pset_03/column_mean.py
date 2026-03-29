""" 
Given a CSV filename, calculate the mean of each column in the CSV 

Requires that filename end with `.csv` and the file contains only integers 

Any empty row element is assumed to be 0 

Examples: 
    column_mean("data1.csv") -> [] 
    column_mean("data2.csv") -> [3.0, -1.0, 0.5, 2.0] 
    column_mean("data3.csv") -> [3.0, 1.0, 0.0] 
    column_mean("data4.csv") -> [2.5, 3.5, 4.5] 
"""
def column_mean(filename : str) -> list[float]: 
    
    with open(filename, "r") as file:
        # read the content's of the file into a string
        content = file.read()
        
        # if the string is empty, return default
        if not content:
            return []
        
        # re-organise the content's from the file to be interpretable list of lists per line 
        content = content.splitlines()
        updated_content = []
        for row in content:
            temp = []
            for i in row.split(","):
                temp.append(int(i))
            updated_content.append(temp)
        
        # find the row with the most columns and store it's length size
        max_cols = len(max(updated_content, key=len))
        
        # ensure all rows have equal amount of elements (columns) - default 0 integer value to fill missing columns
        for row in updated_content:
            while len(row) < max_cols:
                row.append(0)
        
        # calculate column mean
        results = []
        for col in range(max_cols):
            col_mean_val = 0
            for row in range(len(updated_content)):
                col_mean_val += updated_content[row][col]
            col_mean_val = col_mean_val / len(updated_content)
            results.append(col_mean_val)
        
        return results


test_cases = [
    "csv_data/data1.csv",
    "csv_data/data2.csv",
    "csv_data/data3.csv",
    "csv_data/data4.csv"
]

for csv in test_cases:
    print(column_mean(csv))