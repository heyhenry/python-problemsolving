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
        content = file.read()

        # turn file data into list of lists
        content = content.splitlines()
        updated_content = []

        for row in content:
            temp = []
            for i in row.split(","):
                temp.append(i)
            updated_content.append(temp)
        
        # store categories in it's own list variable (for future referencing)
        categories = updated_content[0]
        
        # check if 'name' column exists
        if "name" not in categories:
            return False
        
        # find which index position the 'name' column is located
        name_index = 0
        
        for i in range(len(categories)):
            if categories[i] == "name":
                name_index = i
                break

        # search for requested name
        for row in updated_content:
            if name == row[name_index]:
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
