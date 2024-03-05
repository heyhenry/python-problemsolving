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
def can_construct(ransomNote : str, magazine : str) -> bool:

    can_do = True

    if len(ransomNote) > len(magazine):
        can_do = False
    else:
        temp = ransomNote
        for i in magazine:
            if i in ransomNote:
                temp = temp.replace(i, '', 1)
        if len(temp) == 0:
            can_do = True
        else:
            can_do = False
            
    return can_do

def main():
    print(can_construct(ransomNote = "a", magazine = "b"))
    print(can_construct(ransomNote = "aa", magazine = "ab"))
    print(can_construct(ransomNote = "aa", magazine = "aab"))

if __name__ == "__main__":
    main()