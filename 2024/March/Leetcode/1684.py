"""
1684. Count the Number of Consistent Strings

You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation:All strings are consistent.
Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
 
Constraints:

1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
The characters in allowed are distinct.
words[i] and allowed contain only lowercase English letters.
"""
def count_consistent_strings(allowed : str, words : list[str]) -> int:

    n = len(words)
    fakes = 0

    for word in range(n):
        temp = ''
        for i in words[word]:
            if i not in allowed:
                fakes += 1
                break

    return n - fakes

def main():
    print(count_consistent_strings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))
    print(count_consistent_strings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]))
    print(count_consistent_strings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]))
    print(count_consistent_strings("fstqyienx", ["n","eeitfns","eqqqsfs","i","feniqis","lhoa","yqyitei","sqtn","kug","z","neqqis"]))

if __name__ == "__main__":
    main()