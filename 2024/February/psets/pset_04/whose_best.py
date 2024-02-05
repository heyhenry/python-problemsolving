def whose_best(filename : str) -> str:

    result = ''

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

            # add all inherited key names to keys
            for key, val in name_hierarchy.items():
                for sec_key, sec_val in name_hierarchy.items():
                    if key in sec_val:
                        for v in val:
                            if v not in name_hierarchy[sec_key]:
                                name_hierarchy[sec_key].append(v)

            potential_besties = []
            
            for key, val in name_hierarchy.items():
                name_in_val_counter = 0
                for sec_key, sec_val in name_hierarchy.items():
                     if key in sec_val:
                         name_in_val_counter += 1
                if name_in_val_counter < 1:
                    potential_besties.append(key)

            if len(potential_besties) == 1:
                result = potential_besties[0]
            elif len(potential_besties) < 1:
                result = 'Invalid'
            else:
                result = 'Unknown'

    return result 

def main():
    print(whose_best('3/input1.txt')) # Alice
    print(whose_best('3/input2.txt')) # Invalid
    print(whose_best('3/input3.txt')) # Unknown
    print(whose_best('3/input4.txt')) # Alice
    print(whose_best('3/input5.txt')) # Elmer
    print(whose_best('3/input6.txt')) # Carol
    print(whose_best('3/input7.txt')) # Invalid

if __name__ == "__main__":
    main()