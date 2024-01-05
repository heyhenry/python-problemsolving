"""
2418. Sort the People

You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

 

Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.
Example 2:

Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
 

Constraints:

n == names.length == heights.length
1 <= n <= 103
1 <= names[i].length <= 20
1 <= heights[i] <= 105
names[i] consists of lower and upper case English letters.
All the values of heights are distinct.
"""
def sortPeople(names: list[str], heights: list[int]) -> list[str]:

    order_names = []

    for i in range(len(names)):
        temp = []
        temp.append(heights[i])
        temp.append(names[i])
        order_names.append(temp)
    
    # alternative list comprehension for above ^ 
    # order_names = [(heights[i], names[i]) for i in range(len(names))]

    names.clear()

    for row in sorted(order_names, reverse=True):
        names.append(row[1])

    return names

def main():
    print(sortPeople(["Mary","John","Emma"], heights = [180,165,170]))
    print(sortPeople(["Alice","Bob","Bob"], heights = [155,185,150]))

if __name__ == "__main__":
    main()