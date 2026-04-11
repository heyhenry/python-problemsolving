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
    pass

test_cases = [
    "csv_data/data1.csv",
    "csv_data/data2.csv",
    "csv_data/data3.csv",
    "csv_data/data4.csv"
]

for csv in test_cases:
    print(column_mean(csv))