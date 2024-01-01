"""
9. Just the numbers
Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings. 
The function should return a list with only the integers in the original list in the same order.
"""
def just_numbers(lst : list) -> list:

    result = []

    containsNegatives = False

    for i in lst:
        if isinstance(i , int):
            if i < 0:
                containsNegatives = True

    if containsNegatives == False:

        for i in lst:
            if isinstance(i, int):
                result.append(i)
    
    return result

def main():
    print(just_numbers([1, 3, 4, '4', 3, 10, 'sdf', '55', 66]))
    print(just_numbers([2, 3, 4, 5, 6, 's', 'f', 7, 'td', -1, 'os']))

if __name__ == "__main__":
    main()