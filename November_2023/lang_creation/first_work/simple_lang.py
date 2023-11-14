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

            # variables = {}

            # pattern = re.compile(r"[A-Za-z]")

            # for row in content:
            #     for i in range(len(row)):
            #         if i != len(row)-1:
            #             if row[i] == 'int' and re.fullmatch(pattern, row[i+1]):
            #                 variables[row[i+1]] = 0

            # for row in content:
            #     for i in row:
            #         if i.isdigit():

            xxx = []

            for row in split_content:
                xxx.append(row.split(' = '))

            print(xxx)

def main():
    # print(simple_lang('test_cases/input1.txt'))
    print(simple_lang('test_cases/input2.txt'))

if __name__ == '__main__':
    main()