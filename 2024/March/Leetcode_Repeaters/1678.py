"""
1678. Goal Parser Interpretation

You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

 

Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"
Example 3:

Input: command = "(al)G(al)()()G"
Output: "alGalooG"
 

Constraints:

1 <= command.length <= 100
command consists of "G", "()", and/or "(al)" in some order.
"""
def intepret(command : str) -> str:

    n = len(command)
    s = ''

    left = 0
    
    while len(command) > 0:

        if command[left] == 'G':
            s += 'G'
            command = command.replace('G','',1)
        elif command[left:2] == '()':
            s += 'o'
            command = command.replace('()','',1)
        elif command[left:4] == '(al)':
            s += 'al'
            command = command.replace('(al)','',1)
    
    return s

def main():
    print(intepret(command = "G()(al)"))
    print(intepret(command = "G()()()()(al)"))
    print(intepret(command = "(al)G(al)()()G"))

if __name__ == "__main__":
    main()