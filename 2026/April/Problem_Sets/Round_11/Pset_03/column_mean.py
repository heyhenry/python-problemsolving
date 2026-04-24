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
        for row in content:
            temp = []
            for i in row.split(","):
                temp.append(int(i))
            updated_content.append(temp)
        max_row_length = len(max(updated_content, key=len))
        for row in updated_content:
            while len(row) < max_row_length:
                row.append(0)
        results = []
        for col in range(len(updated_content[0])):
            mean_val = 0
            for row in range(len(updated_content)):
                mean_val += updated_content[row][col]
            mean_val = mean_val / len(updated_content)
            results.append(mean_val)
        return results

test_cases = [
    "csv_data/data1.csv",
    "csv_data/data2.csv",
    "csv_data/data3.csv",
    "csv_data/data4.csv"
]

for csv in test_cases:
    print(column_mean(csv))