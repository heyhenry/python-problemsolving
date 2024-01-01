"""
Returns the maximum even number in each row of `lst`, or `None` if none exists
Note that negatives will be negative when the associated positive is
Examples:
max_even_table([[1, 2, 3]]) -> [2]
max_even([[-4, 3, -1, -6], [1, 3, 5]) -> [-4, None]
max_even_table([[], [1, 4, 6, 2], [-1, -2]]) -> [None, 6, -2]
"""
def max_even_table(lst : list[list[int]]) -> list[int | None]:

    result = []
    # calc_list = []
    max_num = None

    for row in lst:
        temp_list = []
        for i in row:
            if i % 2 == 0:
                temp_list.append(i)
        if temp_list:
            max_num = max(temp_list)
            result.append(max_num)
        elif len(temp_list) == 0:
            max_num = None 
            # reason behind reiterating the None value is based on the python tutor displaying that the max_num is actually 
            # being updated while the final if statements are being processed and never gets referred back to its original value before the for loop, 
            # therefore we need to 'remind' or re-assign the None value based on the desired situational outcome
            result.append(max_num)

    return result

def main():
    print(max_even_table([[1, 2, 3]]))
    print(max_even_table([[-4, 3, -1, -6], [1, 3, 5]]))
    print(max_even_table([[], [1, 4, 6, 2], [-1, -2]]))

if __name__ == "__main__":
    main()

# Completed