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
"""
def can_construct(ransomNote : str, magazine : str) -> bool:

    # dictionaries to hold letter counts
    rnote = {}
    mag = {}

    # populate dictionary with unique letters and their respective counts
    for i in set(ransomNote):
        rnote[i] = ransomNote.count(i)
    for i in set(magazine):
        mag[i] = magazine.count(i)
    # loop through each letter in ransomNote and check count against Magazine 
    for key, val in rnote.items():
        # check if the letter is in magazine
        if key in mag:
            # check if there are enough count of selected letter in magazine
            if val > mag[key]:
                return False
        else:
            return False
    return True

def main():
    print(can_construct(ransomNote = "a", magazine = "b"))
    print(can_construct(ransomNote = "aa", magazine = "ab"))
    print(can_construct(ransomNote = "aa", magazine = "aab"))

if __name__ == "__main__":
    main()