"""
Returns the sum of each row of the table as a list
Examples:
sum_all([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
sum_all([[2], [4, 7], [-1, -2, -4, -5]]) -> [2, 11, -12]
sum_all([[]]) -> []
"""
def sum_all(table : list[list[int]]) -> list[int]:

    result = []
    isFullEmpty = False
    counter = 0

    for i in table:
        sum_value = 0
        for x in i:
            sum_value += x
        result.append(sum_value)
        if len(i) == 0:
            counter += 1
            if counter == len(table):
                isFullEmpty = True

    if isFullEmpty:
        return []
    else:
        return result

def main():

    print(sum_all([[1, 2, 3], [4, 5, 6]]))
    print(sum_all([[2], [4, 7], [-1, -2, -4, -5]]))
    print(sum_all([[]])) # []
    print(sum_all([[], [2, 7]])) # [], [9]

if __name__ == "__main__":
    main()