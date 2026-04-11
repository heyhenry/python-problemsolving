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
        content = content.splitlines()
        updated_content = []
        for row in content:
            temp = []
            for i in row.split(','):
                temp.append(i)
            updated_content.append(temp)
        column_names = updated_content[0]
        updated_content.pop(0)
        name_index = None
        for col in range(len(column_names)):
            if column_names[col] == "name":
                name_index = col
        if name_index is None:
            return False
        for row in updated_content:
            if row[name_index] == name:
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
