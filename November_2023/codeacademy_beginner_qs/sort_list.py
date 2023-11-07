"""
2. Sort a list
Create a function in Python that accepts two parameters. The first will be a list of numbers. 
The second parameter will be a string that can be one of the following values: asc, desc, and none.

If the second parameter is “asc,” then the function should return a list with the numbers in ascending order. 
If it’s “desc,” then the list should be in descending order, and if it’s “none,” it should return the original list unaltered.
"""
def sort_list(nums : list, filter : str):

    result = nums

    if filter == 'asc':
        nums.sort()
    elif filter == 'desc':
        nums.sort(reverse=True)
    
    return result

def main():
    print(sort_list([3,2,5,6,1], 'asc'))
    print(sort_list([3,2,5,6,1], 'desc'))
    print(sort_list([3,2,5,6,1], 'none'))

if __name__ == "__main__":
    main()