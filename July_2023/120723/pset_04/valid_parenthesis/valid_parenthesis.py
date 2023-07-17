def valid_parenthesis(filename: str) -> bool:
    
    with open(filename, 'r') as file:

        read_content = file.read()

        if read_content:

            split_lines = read_content.splitlines()
            
            proper_splits = []

            for row in split_lines:
                temp = []
                for i in row:
                    temp.append(i)
                proper_splits.append(temp)

            print(proper_splits)
                

            opening_braces = proper_splits[0].count('[')
            closing_braces = split_lines.count(']')
            opening_parenthesis = split_lines.count('(')
            closing_parenthesis = split_lines.count(')')

            counter = 0
            # print(split_lines)
            # print('braces: ')
            # print(opening_braces)
            # print(closing_braces)
            # print('parenthesis')
            # print(opening_parenthesis)
            # print(closing_parenthesis)

            if opening_braces == closing_braces:
                counter += 1
            if opening_parenthesis == closing_parenthesis:
                counter += 1
            
            if counter == 2:
                return True
            
            return False

        return False
    
def main():
    print(valid_parenthesis('test_cases/input1.txt'))

if __name__ == '__main__':
    main()