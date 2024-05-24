# alternative to using the global keyword multiple times (a potential solution/alternative)
# sample playground

text = ''

def func_a(text, char):
    text += char
    return text

def func_b(text, char):
    text += char
    return text

while True:
    print("RESULT: " + text)
    user_input = int(input("Type 1 or 2: "))
    if user_input == 1:
        text = func_a(text, 'a')
    elif user_input == 2:
        text = func_b(text, 'b')
    else:
        break

