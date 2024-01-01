def convert_strlst(s : str):

    remove_nl = s.splitlines()
    results = []

    for row in remove_nl:
        line = row.split(',')
        for i in line:
            results.append(int(i))

def main():
    print(convert_strlst('1,-2,1,4\n5'))

if __name__ == "__main__":
    main()