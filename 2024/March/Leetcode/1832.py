"""
1832. Check if the Sentence Is Pangram

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false

Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""
def check_if_pangram(sentence : str) -> bool:

    s = set(sentence)

    return len(s) == 26

def main():
    print(check_if_pangram(sentence = "thequickbrownfoxjumpsoverthelazydog"))
    print(check_if_pangram(sentence = "leetcode"))

if __name__ == "__main__":
    main()
