"""
3. Who's the best
2 / 2
We wanna figure out who has the best name. Fortunately we have a perfect ordering of names (generated by
a magical AI), and just need a way to understand what it spits out. Then print out the best one!
File format: a series of lines of the form Name1 > Name2
Output: one of three things:
1. if a name is better than all others, then that name
2. if multiple names could be the best, then "UNKNOWN"
3. if there's a contradiction (Name1 > Name2, but Name2 > Name1), then "INVALID"
"""
def whose_the_best(filename: str):

    with open(filename, 'r') as file:
        read_content = file.read()
        result = ''
        if read_content:
            split_list = read_content.splitlines()
            content = []
            for row in split_list:
                temp = []
                for i in row.split(' '):
                    temp.append(i)
                content.append(temp)

            names = []

            for row in content: 
                for i in row:
                    if i not in names and i != '<' and i != '>':
                        names.append(i)

            name_hierarchy = {}

            for i in names:
                name_hierarchy[i] = []

            for row in content:
                if row[1] == '<':
                    name_hierarchy[row[2]].append(row[0])
                else:
                    name_hierarchy[row[0]].append(row[2])

            greatest_name = None
            best_name = ''

            # print(name_hierarchy)

            # to find best name if there is evidently only 1 based on greatest amount of names conquered
            for keys, values in name_hierarchy.items():
                if greatest_name is None:
                    greatest_name = len(values)
                    best_name = keys
                elif len(values) > greatest_name:
                    greatest_name = len(values)
                    best_name = keys

            # to find best name when it is more subtle by comparing against the current best name that has conquered the most names
            for keys, values in name_hierarchy.items():
                if best_name in values:
                    best_name = keys

            for keys, values in name_hierarchy.items():
                if keys != best_name and greatest_name == len(values):
                    if values == name_hierarchy[best_name]:
                        best_name = 'Unknown'

            # if there is a contradiction aka the best name that was found was in another key's values then it can be considered invalid
            for keys, values in name_hierarchy.items():
                if keys != best_name and best_name in values:
                    best_name = 'Invalid'
        
        return best_name

def main():
    print(whose_the_best('q3_data/input1.txt')) # Alice
    print(whose_the_best('q3_data/input2.txt')) # Invalid
    print(whose_the_best('q3_data/input3.txt')) # Unknown
    print(whose_the_best('q3_data/input4.txt')) # Alice
    print(whose_the_best('q3_data/input5.txt')) # Elmer
    print(whose_the_best('q3_data/input6.txt')) # Carol
    print(whose_the_best('q3_data/input7.txt')) # Invalid

if __name__ == "__main__":
    main()