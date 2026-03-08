# fullstring: "test"
s = "pwwkew"
subs = []
sub_str = ""
for c in s:
    if c not in sub_str:
        sub_str += c
    else:
        subs.append(sub_str)
        c_index = sub_str.rfind(c)
        sub_str = sub_str[c_index+1:] + c
if sub_str not in subs:
    subs.append(sub_str)
print(subs)
