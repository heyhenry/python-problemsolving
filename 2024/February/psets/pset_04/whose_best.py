def whose_best(filename : str) -> str:

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            split_lines = read_content.splitlines()

            init_content = []

            for row in split_lines:
                init_content.append(row.split(' '))

            name_hierarchy = {}

            # allocate names to their hierachical value
            for row in init_content:
                if row[0] not in name_hierarchy:
                    name_hierarchy[row[0]] = [row[2]]
                else:
                    # dont add values that already exist in a key
                    if row[2] in name_hierarchy[row[0]]:
                        continue
                    else:
                        name_hierarchy[row[0]].append(row[2])

            potential_besties = []

            for key, val in name_hierarchy.items():
                for sec_key, sec_val in name_hierarchy.items():
                     
            

def main():
    # print(whose_best('3/input1.txt'))
    # print(whose_best('3/input2.txt'))
    # print(whose_best('3/input3.txt'))
    # print(whose_best('3/input4.txt'))
    # print(whose_best('3/input5.txt'))
    print(whose_best('3/input6.txt'))
    # print(whose_best('3/input7.txt'))

if __name__ == "__main__":
    main()