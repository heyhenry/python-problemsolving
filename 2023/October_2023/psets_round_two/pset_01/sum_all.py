"""
Returns the sum of each row of the table as a list
Examples:
sum_all([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
sum_all([[2], [4, 7], [-1, -2, -4, -5]]) -> [2, 11, -12]
sum_all([[]]) -> []
"""
def sum_all(table : list[list[int]]) -> list[int]:

    result = []

    for row in table:
        sum_val = 0
        for i in row:
            sum_val += i
        result.append(sum_val)

    return result

def main():
    print(sum_all([[1, 2, 3], [4, 5, 6]]))
    print(sum_all([[2], [4, 7], [-1, -2, -4, -5]]))
    print(sum_all([[]]))

if __name__ == "__main__":
    main()