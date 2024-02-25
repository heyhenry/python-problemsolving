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
def diStringMatch(s : str) -> list[int]:

    # Initial code written after assessing the provided pseudo code I asked to chatgpt ai.
    # n = len(s) + 1
    # perm = [0] * n
    # low, high = 0, n

    # for i in range(0, n-1):
    #     if s[i] == 'I':
    #         perm[i] = low
    #         low += 1
    #     elif s[i] == 'D':
    #         perm[i] = high
    #         high -= 1

    # perm[n-1] = low

    # return perm

    # The pseudo code I given by chatgpt when asked is the following:
    
    # function reconstructPermutation(s):
    #     n = length(s) + 1
    #     perm = [0] * n
    #     low, high = 0, n
        
    #     for i from 0 to n-1:
    #         if s[i] == 'I':
    #             perm[i] = low
    #             low += 1
    #         else:
    #             perm[i] = high
    #             high -= 1
        
    #     perm[n-1] = low  # or high, it doesn't matter
        
    #     return perm

    # After initial attempt at turning it into real code, realised an error in the value for high being a digit too high.
    # Below is the second code written based on the above.
    n = len(s) + 1
    perm = [0] * n
    low, high = 0, len(s)

    for i in range(0, n-1):
        if s[i] == 'I':
            perm[i] = low
            low += 1
        else:
            perm[i] = high
            high -= 1
    
    perm[n-1] = low

    return perm



def main():
    print(diStringMatch(s = "IDID"))
    print(diStringMatch(s = "III"))
    print(diStringMatch(s = "DDI"))

if __name__ == "__main__":
    main()