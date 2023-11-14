"""
Create a simple programming language with python.
In this version it is expected that there are only integer variables and an operand between them (+, -, /, *) for the equation. 
"""
import re

def simple_lang(filename : str):

    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            split_content = read_content.splitlines()

            content = []

            for row in split_content:
                content.append(row.split(' '))

            print_list = []
            
            # stores list of required outputs    
            for row in content:
                if 'print' in row:
                    print_list.append(row)

            # remove print outputs from content list
            for crow in content:
                for prow in print_list:
                    if crow == prow:
                        content.remove(prow)

            variables = []
            chr_pattern = re.compile(r"[A-Za-z]")
            var_found = False
            # find existing values and assign its respective value or equation
            for row in content:
                for i in range(len(row)):
                        if row[i] == 'int' and re.fullmatch(chr_pattern, row[i+1]):
                            variables.append(row[i+1])
                            var_found = True
                del row[:3]
            
            equation_results = []

            for row in content:
                if row[1] == '-':
                    equation_results.append(int(row[0]) - int(row[2]))
                elif row[1] == '+':
                    equation_results.append(int(row[0]) + int(row[2]))
                elif row[1] == '*':
                    equation_results.append(int(row[0]) * int(row[2]))
                else:
                    equation_results.append(int(row[0]) / int(row[2]))

            var_dict = {}

            for i in range(len(variables)):
                var_dict[variables[i]] = equation_results[i]

            
                
def main():
    # print(simple_lang('test_cases/input1.txt'))
    # print(simple_lang('test_cases/input2.txt'))
    print(simple_lang('test_cases/input3.txt')) # 2, 4

if __name__ == '__main__':
    main()