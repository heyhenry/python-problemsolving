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
    with open(filename, "r") as file:
        content = file.read()
        # if table is empty, return defaulted -1
        if not content:
            return -1
        # create list of lists
        content = content.splitlines()
        updated_content = []
        for row in content:
            temp = []
            for i in row.split(","):
                temp.append(i)
            updated_content.append(temp)
        # create a variable to reference column names easily
        categories = updated_content[0]
        # remove the column names list from updated_content
        updated_content.pop(0)
        # search and store indexes for the following column names if found; name, total, first name, last name
        name_index = None
        total_index = None
        first_name_index = None
        last_name_index = None
        for col_name in range(len(categories)):
            if categories[col_name] == "name":
                name_index = col_name
            elif categories[col_name] == "total":
                total_index = col_name
            elif categories[col_name] == "first name":
                first_name_index = col_name
            elif categories[col_name] == "last name":
                last_name_index = col_name
        # conditional search for total value based on a table that contains the 'name' column
        if total_index is not None and name_index is not None:
            for row in updated_content:
                if row[name_index] == name:
                    return row[total_index]
            return -1
        # conditional search for total value based on a table that contains the 'first name' and 'last name' columns
        elif total_index is not None and first_name_index is not None and last_name_index is not None:
            for row in updated_content:
                if f"{row[first_name_index]} {row[last_name_index]}" == name:
                    return row[total_index]
            return -1
        # defaulted return -1 if index variables did not find sufficient values
        else:
            return -1

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