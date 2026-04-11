""" 
Given a filename ending with `csv` 

Returns the total associated with `name` 
If the table has no `total` column or `name` is not found, returns -1 

If the file contains `first name` and `last name` rather than `name` 
Then this function should treat those as concatenated by a space 

Examples: 
    contains_name("table_data/table1.csv", "goblin") -> -1 // no total 
    contains_name("table_data/table2.csv", "bob smith") -> 1234 
    contains_name("table_data/table2.csv", "alice jones") -> 6712 
    contains_name("table_data/table3.csv", "Calvin Harris") -> 64953382 
    contains_name("table_data/table3.csv", "The Weeknd") -> 108390904 
    contains_name("table_data/table3.csv", "Test") -> -1 
"""
def get_name_total(filename : str, name : str) -> int:
    pass

test_cases = [
    ("table_data/table1.csv", "goblin"),
    ("table_data/table2.csv", "bob smith"),
    ("table_data/table2.csv", "alice jones"),
    ("table_data/table3.csv", "Calvin Harris"),
    ("table_data/table3.csv", "The Weeknd"),
    ("table_data/table3.csv", "Test")
]

for case in test_cases:
    print(get_name_total(case[0], case[1]))