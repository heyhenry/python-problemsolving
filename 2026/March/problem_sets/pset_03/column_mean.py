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
    
    with open(filename, "r") as f:
        # read file text and split into list of a row per line
        content = f.read().splitlines()
        
        # exit function is list is empty
        if not content:
            return []
        
        updated_content = []
        # update list of lists to integer values only
        for row in content:
            temp = []
            for i in row.split(","):
                temp.append(int(i))
            updated_content.append(temp)
        
        # find the largest column size out of the given lists
        max_cols = len(max(updated_content, key=len))

        # fill in rows that have less than max column value
        for row in updated_content:
            while len(row) < max_cols:
                row.append(0)

        results = []
        # find the mean sum value of each column of each list
        for col in range(max_cols):
            total_value = 0
            for row in range(len(updated_content)):
                total_value += updated_content[row][col]
            mean_value = total_value / len(updated_content)
            results.append(mean_value)

        # return final results
        return results

test_cases = [
    "csv_data/data1.csv",
    "csv_data/data2.csv",
    "csv_data/data3.csv",
    "csv_data/data4.csv"
]

for csv in test_cases:
    print(column_mean(csv))