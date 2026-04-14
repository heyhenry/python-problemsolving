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
    with open(filename, "r") as file:
        content = file.read()
        
        if not content:
            return []
    
        content = content.splitlines()

        updated_content = []
        max_cols = 0
        for row in content:
            temp = []
            for i in row.split(","):
                temp.append(int(i))
            # find longest column length
            if len(temp) > max_cols:
                max_cols = len(temp)
            updated_content.append(temp)

        # supplement row's with less length than max_cols with 0s
        for row in updated_content:
            while len(row) < max_cols:
                row.append(0)
        
        # calculate column means
        results = []
        for col in range(max_cols):
            mean_value = 0
            for row in range(len(updated_content)):
                mean_value += updated_content[row][col]
            mean_value = mean_value / len(updated_content)
            results.append(mean_value)
        
        return results


test_cases = [
    "csv_data/data1.csv",
    "csv_data/data2.csv",
    "csv_data/data3.csv",
    "csv_data/data4.csv"
]

for csv in test_cases:
    print(column_mean(csv))