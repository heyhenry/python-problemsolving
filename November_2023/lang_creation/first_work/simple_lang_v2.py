import sys

# produces the string output of the given file
def produce_file_string(filename : str):

    with open(filename, 'r') as file:
        read_content = file.read()
        
    return read_content

# parses the file contents into a list of lists (elements per line for each line)
def parse_content_into_listoflists(file_contents : str):

    result = []

    split_content = file_contents.splitlines()

    for row in split_content:
        temp = []
        for i in row.split(' '):
            temp.append(i)
        result.append(temp)

    return result

# akin to .isalpha() and .isdigit(), but for operands and ensures the operand is found in an appropriate location
def contains_operand(s : str) -> bool:
    
    result = False

    for c in range(len(s)):
        if s[c] == '*' and c != 0 and c != len(s)-1:
            result = True
        if s[c] == '-' and c != 0 and c != len(s)-1:
            result = True
        if s[c] == '+' and c != 0 and c != len(s)-1:
            result = True
        if s[c] == '/' and c != 0 and c != len(s)-1:
            result = True

    return result

# removes the operand from a string (does not check if location is appropriate as contains_operand() function is expected to be run first)
def remove_operand_from_string(s:str):

    result = ''

    for c in range(len(s)):
        if s[c] == '*':
            result = s[:c] + s[c+1:]
        if s[c] == '-':
            result = s[:c] + s[c+1:]
        if s[c] == '+':
            result = s[:c] + s[c+1:]
        if s[c] == '/':
            result = s[:c] + s[c+1:]

    return result

def contains_input(s : str) -> bool:

    result = False

    if len(s) == 5 and s == 'input':
        result = True

    return result

def user_input():

    result = input('Provide input (give an integer): ')
    
    # ends program if user input is invalid
    if not result.lstrip('-').isdigit():
        print('NOTICE: INVALID TEST CASE... CRASHING NOW BYE!')
        sys.exit(1)

    return str(result)
    
def validate_variable_name(s : dict) -> bool:

    valid_variable_name = True

    for k, v in s.items():
        if k == 'int':
            valid_variable_name = False
        elif k == 'input':
            valid_variable_name = False
        elif k == 'print':
            valid_variable_name = False

    if not valid_variable_name:
        print('NOTICE: INVALID TEST CASE... CRASHING NOW BYE!')
        sys.exit(1)
    
    return valid_variable_name

def validate_var_type(s : str) -> bool:

    result = False
    valid_types = ['int', 'write']

    if s in valid_types:
        result = True

    return result

# prints the results of the test case file which is encased in a dictionary
def print_results(s : dict):
    
    for k, v in s.items():
        print(v)

def language(filename : str):

    content = produce_file_string(filename)
    content = parse_content_into_listoflists(content)

    vars = {}
    var_types = ['int', 'write']

    for row in content:
        for i in range(len(row)):
            # create a valid key in dict
            if row[i] in var_types:
                vars[row[i+1]] = ''
                for t in range(len(row)):
                    if row[t] == '=':
                        for j in range(t, len(row)-1):
                            if j != len(row)-1:
                                print(vars)
                                vars[row[t-1]] += row[j+1]
                            else:
                                vars[row[t-1]] += row[j]

    result = []
    print(vars)
    if validate_variable_name(vars):

        for k, v in vars.items():
            if contains_operand(v):
                temp = remove_operand_from_string(v)
                if temp.isdigit():
                    result.append(eval(v))
                    vars[k] = eval(v)
                else:
                    var_val = ''
                    updated_equation = ''
                    for c in temp:
                        if c.isalpha():
                            if c in k:
                                var_val = vars[c]
                            # make sure to create the check code for whether c is actually a key in the dict. if it isnt, then crash or w/e
                    for c in range(len(v)):
                        if v[c].isalpha():
                            updated_equation = v[:c] + str(var_val) + v[c+1:]
                    result.append(eval(updated_equation))
                    vars[k] = eval(updated_equation)
            elif contains_input(v):
                vars[k] = user_input()
            else:
                print('NOTICE: INVALID TEST CASE... CRASHING NOW BYE!')
                sys.exit(1)
    
    print_results(vars)

def main():
    
    test_case = sys.argv[1]

    print(language(test_case))

if __name__ == '__main__':
    main()