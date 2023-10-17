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

    desired_extension = '.csv'
    given_extension = filename[-4:]

    if given_extension == desired_extension:

        with open(filename, 'r') as file:

            read_content = file.read()

            if read_content:

                content_splitlines = read_content.splitlines()
                content = []
                for line in content_splitlines:
                    content.append(line.split(','))

                contains_name = False
                name_pos = 0
                
                for i in range(len(content[0])):
                    if content[0][i] == 'name' and len(content[0][i]) == 4:
                        name_pos = i
                        contains_name = True

                if contains_name:

                    for row in range(len(content)):
                        if name in content[row][name_pos]:
                            return True
                    
                    return False

                return False
            
            return False
                
    return False 

def main():

    print(contains_name("tables/table1.csv", "goblin"))
    print(contains_name("tables/table1.csv", "Eve"))
    print(contains_name("tables/table2.csv", "bob"))
    print(contains_name("tables/table3.csv", "Taylor Swift"))
    print(contains_name("tables/table3.csv", "Sabaton"))

if __name__ == "__main__":
    main()