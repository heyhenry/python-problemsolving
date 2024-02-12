"""
389. Find the Difference

You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.

 

Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.
Example 2:

Input: s = "", t = "y"
Output: "y"
 

Constraints:

0 <= s.length <= 1000
t.length == s.length + 1
s and t consist of lowercase English letters.
"""
def findTheDifference(s : str, t : str) -> str:

    result = ''

    s_dict = {}
    t_dict = {}

    for c in s:
        if c not in s_dict:
            s_dict[c] = s.count(c)

    for c in t:
        if c not in t_dict:
            t_dict[c] = t.count(c)

    for key, val in t_dict.items():
        if key not in s_dict:
            result = key

        elif val != s_dict[key]:
            result = key

    return result

def main():
    print(findTheDifference(s = "abcd", t = "abcde"))
    print(findTheDifference(s = "", t = "y"))

if __name__ == "__main__":
    main()