"""
Given a filename ending with `csv`
If that file contains a `name` column, returns if `name` is in that column
Assumes that every row of the data contains a name (a string in the associated column)
Examples:
contains_name("data1.csv", "goblin") -> True
contains_name("data1.csv", "Eve") -> False // uppercase
contains_name("data2.csv", "bob") -> False // no name column
contains_name("data3.csv", "Taylor Swift") -> True
contains_name("data3.csv", "Sabaton") -> False
"""
def contains_name(filename : str, name : str) -> bool:

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            split_nl = read_content.splitlines()

            results = []

            for row in split_nl:
                line = row.split(',')
                temp = []
                for i in line:
                    temp.append(i)
                results.append(temp)
            
            name_col = False
            col_pos = -1

            for row in results[0]:
                col_pos += 1
                if 'name' == row:
                    name_col = True
                    break

            if name_col:

                for row in results:

                    if name == row[col_pos]:

                        return True
            
            return False

def main():
    print(contains_name("tables_csv/table1.csv", "goblin"))
    print(contains_name("tables_csv/table1.csv", "Eve"))
    print(contains_name("tables_csv/table2.csv", "bob"))
    print(contains_name("tables_csv/table3.csv", "Taylor Swift"))
    print(contains_name("tables_csv/table3.csv", "Sabaton"))
    print(contains_name("tables_csv/table4.csv", "goblin")) # True

if __name__ == "__main__":
    main()