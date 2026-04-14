""" 
Returns the sum of each row in the given `.csv` file 

Requires that filename ends with `.csv` 
Also requires that the given CSV file consist of only integers 

Examples: 
    row_sum("data1.csv") -> [] 
    row_sum("data2.csv") -> [4, 5] 
    row_sum("data3.csv") -> [-2, -4, 18] 
    row_sum("data4.csv") -> [6, 9, 12, 15] 
"""
def row_sum(filename : str) -> list[int]:
    with open(filename, "r") as file:
        content = file.read()
        if not content:
            return []
        content = content.splitlines()
        results = []
        for row in content:
            val = 0
            for i in row.split(","):
                val += int(i)
            results.append(val)
        return results
            
test_cases = [
    "csv_data/data1.csv",
    "csv_data/data2.csv",
    "csv_data/data3.csv",
    "csv_data/data4.csv"
]

for data in test_cases:
    print(row_sum(data))