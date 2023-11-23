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