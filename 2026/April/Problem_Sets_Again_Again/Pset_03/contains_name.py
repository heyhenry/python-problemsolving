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
    pass

test_cases = [
    ("table_data/table1.csv", "goblin"),
    ("table_data/table1.csv", "Eve"),
    ("table_data/table2.csv", "bob"),
    ("table_data/table3.csv", "Taylor Swift"),
    ("table_data/table3.csv", "Sabaton")
]

for case in test_cases:
    print(contains_name(case[0], case[1]))
