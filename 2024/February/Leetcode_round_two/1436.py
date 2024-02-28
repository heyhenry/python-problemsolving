def destCity(paths : list[list[str]]) -> str:

    cities = []

    for row in paths:
        for i in row:
            if i not in cities: 
                cities.append(i)

    for row in paths:
        if row[0] in cities:
            cities.remove(row[0])

    return cities[0]

def main():
    print(destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
    print(destCity(paths = [["B","C"],["D","B"],["C","A"]]))
    print(destCity(paths = [["A","Z"]]))

if __name__ == "__main__":
    main()