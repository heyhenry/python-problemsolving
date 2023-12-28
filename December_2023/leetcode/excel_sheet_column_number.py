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
def title_to_number(columnTitle : str) -> int:

    # setup alphabets
    alphabets = {}
    alphabets_s = "XABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # initialize alphabets
    for a in range(1,len(alphabets_s)):
        alphabets[alphabets_s[a]] = a

    # store reversed string of columnTitle
    revised_columnTitle = ''

    # add column title in reverse
    # the reason behind this is to be able to reference each alphabet appropriately i.e. ('ZY' = 10)
    # this is to help with the power to component so that the 2 to the power of 'j' is indicative of the placement
    # of the letter (higher number left to right)
    for i in range(len(columnTitle)-1, -1, -1):
        revised_columnTitle += columnTitle[i]

    result = 0

    # as shown here it is able to reference the correct power to for 26 based on the alphabet position
    for j in range(len(revised_columnTitle)):
        result += alphabets[revised_columnTitle[j]] * (26**j)
    
    return result

def main():
    print(title_to_number("A")) # 1
    print(title_to_number("AB")) # 28 
    print(title_to_number("ZY")) # 701

if __name__ == "__main__":
    main()