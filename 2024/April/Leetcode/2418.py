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
def sort_people(names : list[str], heights : list[int]) -> list[str]:

    n = len(names)
    d = {}
    sorted_names = []

    for i in range(n):
        d[heights[i]] = names[i]

    for key, val in sorted(d.items(), reverse=True):
        sorted_names.append(val)

    for i in range(n):
        names[i] = sorted_names[i]

    return names

def main():
    print(sort_people(names = ["Mary","John","Emma"], heights = [180,165,170]))
    print(sort_people(names = ["Alice","Bob","Bob"], heights = [155,185,150]))

if __name__ == "__main__":
    main()