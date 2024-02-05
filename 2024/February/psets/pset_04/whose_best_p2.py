def whose_best(filename : str) -> str:

    result = ''

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            split_lines = read_content.splitlines()

            content = []

            for row in split_lines:
                content.append(row.split(' '))

            names = {}

            # create initial names dict
            for row in content:
                if row[0] not in names:
                    names[row[0]] = [row[2]]
                elif row[2] not in names[row[0]]:
                    names[row[0]].append(row[2])

            winning_names = []

            # add inherited values to respective keys
            for key, val in names.items():
                key_in_val_counter = 0
                for sec_key, sec_val in names.items():
                    if key in sec_val:
                        key_in_val_counter += 1
                        for v in val:
                            if v not in names[sec_key]:
                                names[sec_key].append(v)
                if key_in_val_counter < 1:
                    winning_names.append(key)

            # assess and provide conclusion
            if len(winning_names) == 1:
                result = winning_names[0]
            elif len(winning_names) > 1:
                result = 'Unknown'
            else:
                result = 'Invalid'

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
