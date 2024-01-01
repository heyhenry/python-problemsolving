lst = [['1','2','3'],['1','2','3'],['1','2','3']]
res = []
for col in range(len(lst[0])):
    sval = ''
    for row in range(len(lst)):
        sval += lst[row][col]
    res.append(sval)
print(res)