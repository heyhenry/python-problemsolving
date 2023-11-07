"""
Valid Parentheses
Your task is to determine if a given collection of parentheses are "valid", meaning that an opening parenthesis
or brace is matched directly with the associated parenthesis or brace.
File format: a single line consisting only of (, [, ), or ]
Output: either true or false
"""
def valid_parenthesis(filename : str):

    with open(filename, 'r') as file:
        
        s = file.read()

        result = True
    
        if s:
            
            stack = [] # will have the opening brackets

            for c in s:
                if c == '(' or c == '[':
                    stack.append(c)
                elif c == ')':
                    if '(' == stack[-1]:
                        stack.remove('(')
                elif c == ']':
                    if '[' == stack[-1]:
                        stack.remove('[')
            
            if len(stack) > 0:
                result = False

        return result

def main():

    print(valid_parenthesis('q1_data/input1.txt')) # true
    print(valid_parenthesis('q1_data/input2.txt')) # false 
    print(valid_parenthesis('q1_data/input3.txt')) # false
    print(valid_parenthesis('q1_data/input4.txt')) # true
    print(valid_parenthesis('q1_data/input5.txt')) # false

if __name__ == "__main__":
    main()