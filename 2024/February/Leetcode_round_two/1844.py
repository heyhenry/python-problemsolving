def replaceDigits(s : str) -> str:

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alpha_book = {}
    result = ''

    for i in range(len(alphabet)):
        alpha_book[i] = alphabet[i]

    shifts = []

    temp = []
    counter = 0
    for c in s:
        counter += 1
        if counter == 2:
            temp.append(c)
            shifts.append(temp)
            temp = []
            counter = 0
        else:
            temp.append(c)
        
    storage = []
    for key, val in alpha_book.items():
        for i in shifts:
            if val == i[0]:
                result += i[0]
                result += alpha_book[int(key)+int(i[1])]

    if len(result) != len(s):
        result += s[-1]

    return result


def main():
    print(replaceDigits(s = "a1c1e1"))
    print(replaceDigits(s = "a1b2c3d4e"))

if __name__ == "__main__":
    main()