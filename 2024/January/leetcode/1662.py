"""
1662. Check If Two String Arrays are Equivalent

Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

 

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
 

Constraints:

1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.
"""
def arrayStringsAreEqual(word1: list[str], word2: list[str]) -> bool:

    result = True
    first_word = [i for element in word1 for i in element]
    second_word = [i for element in word2 for i in element]

    if len(first_word) != len(second_word):
        result = False
    else:
        counter = -1

        while counter < len(first_word)-1 and result == True:
            
            counter += 1

            if first_word[counter] != second_word[counter]:
                result = False

    return result

def main():
    # print(arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"]))
    # print(arrayStringsAreEqual(word1 = ["a", "cb"], word2 = ["ab", "c"]))
    print(arrayStringsAreEqual(word1 = ["abc", "d", "defg"], word2 = ["abcddefg"]))

if __name__ == "__main__":
    main()