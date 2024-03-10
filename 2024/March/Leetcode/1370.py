"""
1370. Increasing Decreasing String

You are given a string s. Reorder the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.

Example 1:

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
Example 2:

Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters.
"""
def sort_string(s : str) -> str:

    result = ''
    n = len(s)
    hs = sorted(set(s))

    while len(result) < n:

        for i in hs:
            if i in s:
                result += i
                s = s.replace(i,'',1)
        for i in sorted(hs, reverse=True):
            if i in s:
                result += i
                s = s.replace(i,'',1)
            
    return result

def main():
    print(sort_string(s = "aaaabbbbcccc"))
    print(sort_string(s = "rat"))

if __name__ == "__main__":
    main()