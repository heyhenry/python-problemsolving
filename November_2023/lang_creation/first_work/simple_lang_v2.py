import sys

# produces the string output of the given file
def produce_file_string(filename : str):

    with open(filename, 'r') as file:
        read_content = file.read()
        
    return read_content

def parse_content_into_listoflists(file_contents : str):

    result = []

    split_content = file_contents.splitlines()

    for row in split_content:
        temp = []
        for i in row.split(' '):
            temp.append(i)
        result.append(temp)

    return result

def contains_operand(s:str):
    
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

def language(filename : str):

    content = produce_file_string(filename)
    content = parse_content_into_listoflists(content)

    vars = {}

    for row in content:
        for i in range(len(row)):
            if row[i] == 'int':
                vars[row[i+1]] = ''
            if row[i] == '=':
                for j in range(i, len(row)-1):
                    if j != len(row)-1:
                        vars[row[i-1]] += row[j+1]
                    else:
                        vars[row[i-1]] += row[j]

    result = []

    for k, v in vars.items():
        if contains_operand(v):
            temp = remove_operand_from_string(v)
            print(temp)

    print(vars)

def main():
    
    test_case = sys.argv[1]

    print(language(test_case))

if __name__ == '__main__':
    main()
