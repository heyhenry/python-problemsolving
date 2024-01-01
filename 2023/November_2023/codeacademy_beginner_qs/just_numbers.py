"""
9. Just the numbers
Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings. 
The function should return a list with only the integers in the original list in the same order.
"""
def just_numbers(lst : list):

    result = []

    for i in lst:
        if isinstance(i, int) and i > 0:
            result.append(i)
    
    return result

def main():
    print(just_numbers([2,3,4,'s',4,'peewee',-1]))
    print(just_numbers(['walla','palla',-2,-5,2]))

if __name__ == "__main__":
    main()