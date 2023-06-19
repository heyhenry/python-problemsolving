"""
Returns nothing
Modifies table in place to double each number
Examples:
double([[1, 2], [3, 4, 5]]) changes lst to [[2, 4], [6, 8, 10]]
double([[-1], [-2], [0, 0]]) changes lst to [[-1], [-2], [0, 0]]
double([[]]) does "nothing"
"""
def double(table : list[list[int]]):

    updated_table = []

    for row in table: 
        temp_list = []
        for i in row:
            i = i * 2
            temp_list.append(i)
        updated_table.append(temp_list)
    
    table.clear()

    table.append(updated_table)

def main():

    list_one = [[1, 2], [3, 4, 5]]
    list_two = [[-1], [-2], [0, 0]]
    list_three = [[]]

    print('Before:')
    print(list_one)
    print(list_two)
    print(list_three)

    double(list_one)
    double(list_two)
    double(list_three)

    print('After:')
    print(list_one)
    print(list_two)
    print(list_three)

if __name__ == "__main__":
    main()

# Completed