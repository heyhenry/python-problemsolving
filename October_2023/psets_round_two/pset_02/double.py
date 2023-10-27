"""
Returns nothing
Modifies table in place to double each number
Examples:
double([[1, 2], [3, 4, 5]]) changes lst to [[2, 4], [6, 8, 10]]
double([[-1], [-2], [0, 0]]) changes lst to [[-1], [-2], [0, 0]]
double([[]]) does "nothing"
"""
def double(table : list[list[int]]):

    lst = []

    for row in table:
        temp = []
        for i in row:
            temp.append(i*2)
        lst.append(temp)
    
    table.clear()

    table += lst

def main():
    
    lst_1 = [[1, 2], [3, 4, 5]]
    lst_2 = [[-1], [-2], [0, 0]]
    lst_3 = [[]]

    double(lst_1)
    double(lst_2)
    double(lst_3)

    print(lst_1)
    print(lst_2)
    print(lst_3)

if __name__ == "__main__":
    main()