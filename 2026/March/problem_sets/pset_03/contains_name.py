""" 
Given a filename ending with `csv` 

If that filecontains a `name` column, returns if `name` is in that column 

Examples: 
    contains_name("table1.csv", "goblin") -> True 
    contains_name("table1.csv", "Eve") -> False // uppercase 
    contains_name("table2.csv", "bob") -> False // no name column 
    contains_name("table3.csv", "Taylor Swift") -> True 
    contains_name("table3.csv", "Sabaton") -> False 
"""
def contains_name(filename : str, name : str) -> bool:
    with open(filename, "r") as file:
        # read and store file text 
        content = file.read()

        # exit function early if file is empty
        if not content:
            return False

        # create a list that appends each line as an element
        content = content.splitlines()
        
        updated_content = []
        # place separate each row and column accordingly per line
        for row in content:
            temp = []
            for i in row.split(","):
                temp.append(i)
            updated_content.append(temp)
        
        # if name column doesn't exist, return False
        if "name" not in updated_content[0]:    
            return False
        
        # find which column index holds the name column
        name_column_index = 0
        for i in range(len(updated_content[0])):
            if updated_content[0][i] == "name":
                name_column_index = i
                break

        # search for the desired name
        for row in updated_content:
            if row[name_column_index] == name:
                return True
            
        return False

test_cases = [
    ("table_data/table1.csv", "goblin"),
    ("table_data/table1.csv", "Eve"),
    ("table_data/table2.csv", "bob"),
    ("table_data/table3.csv", "Taylor Swift"),
    ("table_data/table3.csv", "Sabaton")
]

for case in test_cases:
    print(contains_name(case[0], case[1]))
