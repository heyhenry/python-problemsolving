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

    if len(magazine) < len(ransomNote):
        return False
    
    letters = {}

    for i in magazine:
        if i not in letters:
            letters[i] = 1
        else:
            letters[i] += 1

    for i in ransomNote:
        if i in letters and letters[i] > 0:
            letters[i] -= 1
            print(letters)
        else:
            return False
        
    return True

def main():
    print(can_construct(ransomNote = "a", magazine = "b"))
    print(can_construct(ransomNote = "aa", magazine = "ab"))
    print(can_construct(ransomNote = "aa", magazine = "aab"))

if __name__ == "__main__":
    main()