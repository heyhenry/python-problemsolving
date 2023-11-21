"""
Create a simple programming language with python.
In this version it is expected that there are only integer variables and an operand between them (+, -, /, *) for the equation. 
"""
import re
import os

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

            var_dict = {}

            # find existing values and assign its respective value or equation
            for row in content:
                num1 = None
                num2 = None
                operand = None
                var_val = 0
                for i in range(len(row)):
                    if row[i] == 'int' and re.fullmatch(chr_pattern, row[i+1]):
                        variables.append(row[i+1])
                        for j in range(i+3, len(row)):
                            if num1 is None:
                                num1 = row[j]
                            elif operand is None:
                                operand = row[j]
                            elif num2 is None:
                                num2 = row[j]
                        if num1.isdigit() == False:
                            num1 = var_dict[num1]
                        elif num2.isdigit() == False:
                            num2 = var_dict[num2]
                        
                        if operand == '+':
                            var_val = int(num1) + int(num2)
                        elif operand == '-':
                            var_val = int(num1) - int(num2)
                        elif operand == '*':
                            var_val = int(num1) * int(num2)
                        elif operand == '/':
                            var_val = int(num1) / int(num2)
                        var_dict[row[i+1]] = var_val
                            
                del row[:3]

            # id = filename[16:-4]

            # new_filename = 'test_cases/solution' + id + '.txt' 

            filename_index = filename.rfind('/')

            temp_filename = filename[filename_index+1:]

            selected_filename = temp_filename.replace('input', 'solution')

            dir_index = filename.rfind('/')
            dir_name = filename[:dir_index+1]

            new_filename = dir_name + selected_filename

            with open(new_filename, 'w') as nfile:

                # prints out var_dict values
                for k, v in var_dict.items():
                    nfile.write(str(v) + '\n')
                   
def main():
    print(simple_lang('ts/input1.txt')) # returns 2, 4
    # print(simple_lang('test_cases/input2.txt')) # returns 2
    # print(simple_lang('test_cases/input3.txt')) # returns 2, 4
    # print(simple_lang('test_cases/input4.txt')) # returns 2, 3

if __name__ == '__main__':
    main()