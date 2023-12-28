def get_name_total(filename : str, name : str) -> int:
"""
Given a filename ending with `csv`
Returns the total associated with `name`
If the table has no `total` column or `name` is not found, returns -1
If the file contains `first name` and `last name` rather than `name`
Then this function should treat those as concatenated by a space
Examples:
contains_name("data1.csv", "goblin") -> -1 // no total
contains_name("data2.csv", "bob smith") -> 1234
contains_name("data2.csv", "alice jones") -> 6712
contains_name("data3.csv", "Calvin Harris") -> 64953382
contains_name("data3.csv", "The Weeknd") -> 108390904
contains_name("data3.csv", "Test") -> -1
"""