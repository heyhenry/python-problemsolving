namess = [['Bob', 'Joker'], ['Bob', 'Joker']]
names = [['Bob', 'Joker'], ['Bob'], ['Bob', 'Joker']]

counter = 0
unknown_checker = 0
is_unknown = True
while counter < len(names):
    for n in range(len(names)):
        if n != counter:
            if set(names[counter]) == set(names[n]):
                unknown_checker += 1
    counter += 1
if unknown_checker == len(names):
    is_unknown = True
else:
    is_unknown = False
    
if is_unknown == True:
    print('Unknown')
else:
    print('Nah we know')