
"""
Returns nothing
Modifies table in place to double each number
Examples:
double([[1, 2], [3, 4, 5]]) changes lst to [[2, 4], [6, 8, 10]]
double([[-1], [-2], [0, 0]]) changes lst to [[-2], [-4], [0, 0]]
double([[]]) does "nothing"
"""
def double(table : list[list[int]]):

    doubled_table = []

    for row in table:
        temp = []
        for i in row:
            temp.append(i*2)
        doubled_table.append(temp)

    table.clear()

    table += doubled_table 

def main():
    
    lst1 = [[1, 2], [3, 4, 5]]
    lst2 = [[-1], [-2], [0, 0]]
    lst3 = [[]]
    
    double(lst1)
    double(lst2)
    double(lst3)

    print(lst1)
    print(lst2)
    print(lst3)

if __name__ == "__main__":
    main()
