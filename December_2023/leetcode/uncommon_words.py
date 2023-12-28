"""
884. Uncommon Words from Two Sentences

A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]
 

Constraints:

1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.
"""
def uncommon_words(s1 : str, s2 : str) -> list[str]:

    results = []

    new_s = s1.split(' ') + s2.split(' ')

    for i in new_s:
        if new_s.count(i) < 2:
            results.append(i)
         
    return results

def main():
    print(uncommon_words("this apple is sweet", "this apple is sour"))
    print(uncommon_words("apple apple","banana"))

if __name__ == "__main__":
    main()

# Note: I don't approve of the given output for test case 2. I believe it should be both Apple and Banana, contrary to the belief of Leetcode.