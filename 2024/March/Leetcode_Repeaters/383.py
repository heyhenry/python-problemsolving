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

    result = True

    m_dict = {}
    rn_dict = {}

    for i in ransomNote:
        if i not in rn_dict:
            rn_dict[i] = 1
        else:
            rn_dict[i] += 1

    for i in magazine:
        if i not in m_dict:
            m_dict[i] = 1
        else:
            m_dict[i] += 1

    for key, val in rn_dict.items():
        if key in m_dict and val > m_dict[key]:
            result = False
            break
        elif key not in m_dict:
            result = False
            break

    return result  

def main():
    print(can_construct(ransomNote = "a", magazine = "b"))
    print(can_construct(ransomNote = "aa", magazine = "ab"))
    print(can_construct(ransomNote = "aa", magazine = "aab"))

if __name__ == "__main__":
    main()