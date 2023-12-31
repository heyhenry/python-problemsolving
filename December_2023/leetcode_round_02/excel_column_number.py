"""
171. Excel Sheet Column Number

Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
 

Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
"""
def title_to_number(columnTitle: str) -> int:

    result = 0
    alphabet = {}

    for i in range(ord('A'), ord('Z')+1):
        alphabet[chr(i)] = ''

    counter = 1
    for i in alphabet:
        alphabet[i] = counter
        counter += 1

    rev_columnTitle = columnTitle[::-1]

    for c in range(len(rev_columnTitle)):
        
        result += alphabet[rev_columnTitle[c]] * (26**c)

    return result


def main():
    print(title_to_number("A"))
    print(title_to_number("AB"))
    print(title_to_number("ZY"))

if __name__ == "__main__":
    main()