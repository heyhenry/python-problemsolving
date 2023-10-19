"""
4. Count the vowels in a string
Create a function in Python that accepts a single word and returns the number of vowels in that word. 
In this function, only a, e, i, o, and u will be counted as vowels — not y.
"""

def count_vowels(s : str) -> int:

    result = 0

    for c in s:
        if c in 'aeiou':
            result += 1
    
    return result

def main():
    print(count_vowels('yogabagaba')) # 5
    print(count_vowels('yooiyo')) # 4
    print(count_vowels('aeiouy')) # 5
    print(count_vowels('yaeisou')) # 5
    print(count_vowels('pygmy')) # 0

if __name__ == "__main__":
    main()