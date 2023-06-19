# Returns nothing
# Modifies table in place to double each number
# Examples:
# double([[1, 2], [3, 4, 5]]) changes lst to [[2, 4], [6, 8, 10]]
# double([[-1], [-2], [0, 0]]) changes lst to [[-1], [-2], [0, 0]]
# double([[]]) does "nothing"

def double(table : list[list[int]]):

    updated_table = []

    for row in table:
        new_table = []
        for num in row:
            new_num = num * 2
            new_table.append(new_num)
        updated_table.append(new_table)

    for i in range(len(table)):
        table[i] = updated_table[i]

def main():

    first_list = [[1, 2], [3, 4, 5]]
    second_list = [[-1], [-2], [0, 0]]
    third_list = [[]]

    # print lists before results
    print("Before executing the double function on lists:")
    print(first_list)
    print(second_list)
    print(third_list)
    
    print('')
    
    print("After executing the double function on lists:")
    
    # perform action
    double(first_list)
    double(second_list)
    double(third_list)

    # print new results
    print(first_list)
    print(second_list)
    print(third_list)

if __name__ == "__main__":
    main()