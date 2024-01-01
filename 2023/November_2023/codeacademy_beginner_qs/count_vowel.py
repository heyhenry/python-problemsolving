"""
4. Count the vowels in a string
Create a function in Python that accepts a single word and returns the number of vowels in that word. 
In this function, only a, e, i, o, and u will be counted as vowels — not y.
"""
def count_vowels(s : str):

    result = 0

    for c in s:
        if c in 'aeiou':
            result += 1
    
    return result

def main():
    print(count_vowels('alieo'))
    print(count_vowels('ypypypeypysdo'))
    print(count_vowels('ypoypsa'))
    print(count_vowels('yy'))

if __name__ == "__main__":
    main()