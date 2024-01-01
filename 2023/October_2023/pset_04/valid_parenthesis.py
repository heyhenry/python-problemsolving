"""
Your task is to determine if a given collection of parentheses are "valid", meaning that an opening parenthesis
or brace is matched directly with the associated parenthesis or brace.
File format: a single line consisting only of (, [, ), or ]
Output: either true or false
"""

# brain storming/thinking
# if there is any number between 2 numbers, then it is considered to be 'interrupted' --> which means that it can not be a possible pair.


# txt = '([)]'
# count = 0
# ans = False

# for c in txt:
#     if c == '(':
#         count += 1
#     elif c == ")":
#         count -= 1
#         if count < 0:
#             ans = False
# ans = True

# print(ans)

def isValid (sequence: str):
    '''
    Function to pair if sequence contains valid parenthesis
    :param sequence: Sequence of brackets
    :return: True is sequence is valid else False
    '''
    stack = []
    opening = set('([{')
    closing = set(')]}')
    pair = {')' : '(' , ']' : '[' , '}' : '{'}
    for i in sequence :
        if i in opening :
            stack.append(i)
        if i in closing :
            if not stack :
                return False
            elif stack.pop() != pair[i] :
                return False
            else :
                continue
    if not stack :
        return True
    else :
        return False

def main():
    sequence = '([)]'
    print(f'Is {sequence} valid ? : {isValid(sequence)}')
    # sequence1 = '{[()]}{]{}}'
    # print(f'Is {sequence1} valid ? : {isValid (sequence1)}')

if __name__ == '__main__':
    main()

# Resource used to find the solution.. 
# Link: https://favtutor.com/blogs/valid-parentheses#:~:text=To%20solve%20a%20valid%20parentheses,it%20with%20the%20starting%20bracket.
