"""
3. Who's the best

We wanna figure out who has the best name. Fortunately we have a perfect ordering of names (generated by
a magical AI), and just need a way to understand what it spits out. Then print out the best one!
File format: a series of lines of the form Name1 > Name2
Output: one of three things:
1. if a name is better than all others, then that name
2. if multiple names could be the best, then "UNKNOWN"
3. if there's a contradiction (Name1 > Name2, but Name2 > Name1), then "INVALID"
"""
import sys

def whose_best(filename : str):

    greatest_name = ''
    result = ''

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            split_lines = read_content.splitlines()
            content = []
            for row in split_lines:
                content.append(row.split(' '))
            
            names = {}

            # create names dictionary keys
            for row in content:
                for i in row:
                    if i != '>' and i not in names:
                        names[i] = []
            
            # add initial values for each key
            for row in content:
                if row[2] not in names[row[0]]:
                    names[row[0]].append(row[2])

            # add inherited values for each key
            for key, values in names.items():
                for second_key, second_values in names.items():
                    if key in second_values:
                        for v in values:
                            if v not in second_key:
                                names[second_key].append(v)
            
            # find potential best name
            for key, values in names.items():
                if greatest_name == '' or greatest_name in values:
                    greatest_name = key

            # cross examine the keys and values for multiple best names
            best_names = []
            
            for key, values in names.items():
                a_name = ''
                counter = 0
                for second_key, second_values in names.items():
                    if key not in second_values:
                        a_name = key
                        counter += 1
                if counter == len(names):
                    best_names.append(a_name)
            
            # utilise validation algorithm above to determine appropriate result
            if len(best_names) > 1:
                result = 'UNKNOWN'
            elif len(best_names) < 1:
                result = 'INVALID'
            else:
                result = greatest_name
            
    return result

def main():
    print(whose_best(sys.argv[1]))

if __name__ == "__main__":
    main()