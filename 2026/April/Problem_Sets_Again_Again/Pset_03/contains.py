""" 
Returns whether the given word appears in a `.fakeletters` file 

Requires that `filename` ends with `.fakeletters` 
 
Examples: 
    contains("test1.fakeletters", "b") -> True 
    contains("test1.fakeletters", "d") -> False 
    contains("test2.fakeletters", "wor") -> False 
    contains("test2.fakeletters", "hello") -> True 
    contains("test3.fakeletters", "") -> False 
"""
def contains(filename : str, word : str) -> bool: 
    pass

if __name__ == "__main__":
    test_cases = [
        ("test1.fakeletters", "b"),
        ("test1.fakeletters", "d"),
        ("test2.fakeletters", "wor"),
        ("test2.fakeletters", "hello"),
        ("test3.fakeletters", ""),
    ]

    for i in range(len(test_cases)):
        print(contains(f"fakeletters/{test_cases[i][0]}", test_cases[i][1]))