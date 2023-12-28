"""
Returns the alphabetically-ordered string from a dictionary of letters and
counts
Note that each key of the dictionary must be a single lowercase letter
Examples:
ordered_string({}) -> ""
ordered_string({'a' : 3, 'b' : 2}) -> "aaabb"
ordered_string({'d' : 1, 'a' : 2', 'c' : 3}) -> "aacccd"
ordered_string({'z' : 5, 'd' : 2, 'a' : 3, 'x' : 2} -> "aaaddxxzzzzz"
"""
def ordered_string(d : dict[str, int]) -> str:



def main():
    print(ordered_string({}))
    print(ordered_string({'a' : 3, 'b' : 2}))
    print(ordered_string({'d' : 1, 'a' : 2, 'c' : 3}))
    print(ordered_string({'z' : 5, 'd' : 2, 'a' : 3, 'x' : 2}))

if __name__ == "__main__":
    main()
