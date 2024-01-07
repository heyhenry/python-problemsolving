"""
942. DI String Match

A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

 

Example 1:

Input: s = "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: s = "III"
Output: [0,1,2,3]
Example 3:

Input: s = "DDI"
Output: [3,2,0,1]
 

Constraints:

1 <= s.length <= 105
s[i] is either 'I' or 'D'.
"""
def diStringMatch(s: str) -> list[int]:

    results = []
    perm = []

    for i in range(0, len(s)+1):
        perm.append(i)

    for i in range(len(s)):
        if perm[i] < perm[i + 1]:
            if s[i] == 'I':
                results.append(i)
        elif perm[i] > perm[i + 1]:
            if s[i] == 'D':
                results.append(i)

    return results

def main():
    print(diStringMatch(s = "IDID"))
    print(diStringMatch(s = "III"))
    print(diStringMatch(s = "DDI"))

if __name__ == "__main__":
    main()