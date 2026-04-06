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
            for i in row.split(","):
                temp.append(i)
            updated_content.append(temp)
        
        categories = updated_content[0]

        if "name" in categories:
            
            name_index = None

            for col_name in range(len(categories)):
                if categories[col_name] == "name":
                    name_index = col_name

            for row in range(1, len(updated_content)):
                if updated_content[row][name_index] == name:
                    return True
                
            return False
        
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
