"""
2. Sort a list
Create a function in Python that accepts two parameters. The first will be a list of numbers. 
The second parameter will be a string that can be one of the following values: asc, desc, and none.

If the second parameter is “asc,” then the function should return a list with the numbers in ascending order. 
If it’s “desc,” then the list should be in descending order, and if it’s “none,” it should return the original list unaltered.
"""
# asc -> smallest to largest
# desc -> largest to smallest
# none -> original
def sort_list(lst : list, sort : str) -> list:
        
    new_list = []
    lst_len = len(lst)
    count = 1

    if sort == 'asc':
        while len(lst) != 0:
            val = min(lst)
            new_list.append(val)
            lst.remove(val)
            count += 1
    elif sort == 'desc':
        while len(lst) != 0:
            val = max(lst)
            new_list.append(val)
            lst.remove(val)
            count += 1        
    elif sort == 'none':
        new_list += lst

    return new_list     

def main():
    print(sort_list([3,2,1], 'asc'))
    print(sort_list([7,6,8], 'desc'))
    print(sort_list([420,69,420,1], 'none'))

if __name__ == "__main__":
    main()