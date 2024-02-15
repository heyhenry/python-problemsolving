"""
1844. Replace All Digits with Characters

You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.

There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.

For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).

Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.

 

Example 1:

Input: s = "a1c1e1"
Output: "abcdef"
Explanation: The digits are replaced as follows:
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('c',1) = 'd'
- s[5] -> shift('e',1) = 'f'
Example 2:

Input: s = "a1b2c3d4e"
Output: "abbdcfdhe"
Explanation: The digits are replaced as follows:
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('b',2) = 'd'
- s[5] -> shift('c',3) = 'f'
- s[7] -> shift('d',4) = 'h'
 

Constraints:

1 <= s.length <= 100
s consists only of lowercase English letters and digits.
shift(s[i-1], s[i]) <= 'z' for all odd indices i.
"""
def replaceDigits(s : str) -> str:
    results = ''
    new_s = ''
    alphabet_str = 'abcdefghijklmnopqrstuvwxyz'
    pairs = []
    equal_pairs = True

    if len(s) % 2 != 0:
        equal_pairs = False

    if not equal_pairs:

        for i in range(0, len(s[:-1]), 2):
            pairs.append([s[i], s[i+1]])

        for p in pairs:
            current_position = alphabet_str.rfind(p[0])
            new_s += alphabet_str[current_position+int(p[1])]
        
        for p in range(len(pairs)):
            pairs[p][1] = new_s[p]
        
        for pair in pairs:
            for p in pair:
                results += p

        results += s[-1]
        
    else:

        for i in range(0, len(s), 2):
            pairs.append([s[i], s[i+1]])

        for p in pairs:
            current_position = alphabet_str.rfind(p[0])
            new_s += alphabet_str[current_position+int(p[1])]

        for p in range(len(pairs)):
            pairs[p][1] = new_s[p]

        for pair in pairs:
            for p in pair:
                results += p
        
    return results

def main():
    print(replaceDigits(s = "a1c1e1"))
    print(replaceDigits(s = "a1b2c3d4e"))

if __name__ == "__main__":
    main()