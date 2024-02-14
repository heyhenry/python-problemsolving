"""
383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""
def canConstruct(ransomNote : str, magazine : str) -> bool:

    # solution 1
    # result = True

    # for i in ransomNote:
    #     if magazine.count(i) < ransomNote.count(i):
    #         result = False

    # return result

    # solution 2
    result = True
    ransom = {}
    maga = {}

    for i in ransomNote:
        if i not in ransom:
            ransom[i] = 1
        else:
            ransom[i] += 1

    for i in magazine:
        if i not in maga:
            maga[i] = 1
        else:
            maga[i] += 1

    for key in ransom:
        if key not in maga:
            result = False
        elif maga[key] < ransom[key]:
            result = False

    return result

def main():
    print(canConstruct(ransomNote = "a", magazine = "b"))
    print(canConstruct(ransomNote = "aa", magazine = "ab"))
    print(canConstruct(ransomNote = "aa", magazine = "aab"))

if __name__ == "__main__":
    main()