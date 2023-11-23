s = 'LVIII'
list_s = list(s)
result = 0
counter = 0

for c in range(len(list_s)):
    if counter == len(list_s):
        break
    if list_s[c] == 'L': 
        print('L triggered')
        result += 50
        counter += 1
    elif list_s[c] == 'V':
        print('V triggered')
        result += 5
        counter += 1
    elif list_s[c] == 'I':
        if c != len(list_s) - 1:
            if list_s[c+1] == 'V':
                print('IV triggered')
                result += 4
                counter += 2
            else:
                print('I triggered')
                result += 1
                counter += 1
        else:
            print('I triggered aswell')
            result += 1
            counter += 1
    elif list_s[c] == 'M':
        if c == 0:
            print('M triggered')
            result += 1000
            counter += 1
        elif list_s[c-1] == 'C':
            print('CM triggered')
            result += 900
            counter += 2
    elif list_s[c] == 'X':
        if c != len(list_s) - 1:
            if list_s[c+1] == 'C':
                print('XC triggered')
                result += 90
                counter += 2
            
print(result)

# some notes to self about solving the problem - Please READ

# The problem solution strictly caters to the provided roman numerals that are being tested on.
# It uses a counter system to realise when all the characters in the string has been accounted for.
# Currently the string has been altered to be a list due to the notion of utilising list's built in functions (remove, replace and pop), 
# however it hasnt gone well as it affected the static iteration course of the list_s itself as elements were beinga actively removed. 
# Further more it just seemed to cause more confusion and code chaos, encroaching upon code readability.

# I will test the alternative usage of a new list rather than a counter, but I think the counter is still cleaner and requires less code at the end.
# Also remember to transfer the final code solution to the actual problem file instead of residing in the test file.
# Might also remove the list system generally, if maintaining the counter system as it seems to be unnessary, but will trial after break. 