# Returns the sum of each row of the table as a list
# Examples:
# sum_all([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
# sum_all([[2], [4, 7], [-1, -2, -4, -5]]) -> [2, 11, -12]
# sum_all([[]]) -> []

def sum_all(table : list[list[int]]) -> list[int]:

    sum_list = []

    for row in table:
        sum_value = 0
        for num in row:
            sum_value += num
        sum_list.append(sum_value)
    
    return sum_list

def main():

    print(sum_all([[1, 2, 3], [4, 5, 6]]))
    print(sum_all([[2], [4, 7], [-1, -2, -4, -5]])) 
    print(sum_all([[]]))
    print(sum_all([[0]]))

if __name__ == "__main__":
    main()