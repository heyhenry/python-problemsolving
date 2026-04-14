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
        # put file contents into a singular elemental string in a list
        content = file.read()
        # if file is empty, return an empty list
        if not content:
            print("SDKFJ")
            return []
        # update the content's list into list of lists where each line is a new list
        content = content.splitlines()
        # house list of list as list of int elements per line, stored in updated_content's list
        updated_content = []
        for row in content:
            temp = []
            for i in row.split(","):
                temp.append(int(i))
            updated_content.append(temp)
        # find the largest column length
        cols = len(updated_content[0])
        for row in range(1, len(updated_content)):
            if len(updated_content[row]) > cols:
                cols = len(updated_content[row])
        # check and flag if all columns have the same length
        is_uneven_cols = False
        for row in range(1, len(updated_content)):
            if len(updated_content[row]) != len(updated_content[0]):
                is_uneven_cols = True
                break
        # update all lists to have the same column length (use 0 as the placeholder element)
        if is_uneven_cols:
            for row in updated_content:
                while len(row) != cols:
                    row.append(0)
        # calculate column means
        results = []
        for col in range(cols):
            mean_value = 0
            for row in range(len(updated_content)):
                mean_value += updated_content[row][col]
            mean_value = mean_value / len(updated_content)
            results.append(mean_value)
        # return results
        return results

test_cases = [
    "csv_data/data1.csv",
    "csv_data/data2.csv",
    "csv_data/data3.csv",
    "csv_data/data4.csv"
]

for csv in test_cases:
    print(column_mean(csv))