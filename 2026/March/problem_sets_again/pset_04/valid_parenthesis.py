"""
1. Valid Parentheses
Your task is to determine if a given collection of parentheses are "valid", meaning that an opening parenthesis
or brace is matched directly with the associated parenthesis or brace.
File format: a single line consisting only of (, [, ), or ]
Output: either true or false
"""
def is_valid(filename : str) -> bool:
    with open(filename, "r") as file:
        content = file.read()
        parenthesis_dict = {")": "(", "]": "["}
        stack = []
        for i in content:
            if i in parenthesis_dict.values():
                stack.append(i)
            else:
                if stack and parenthesis_dict[i] == stack[-1]:
                    stack.pop()
        if stack:
            return False
        return True

test_cases = [
    "test_cases/1/input1.txt", # true
    "test_cases/1/input2.txt", # false
    "test_cases/1/input3.txt", # false
    "test_cases/1/input4.txt", # true 
    "test_cases/1/input5.txt" # false
]

for test in test_cases:
    print(is_valid(test))