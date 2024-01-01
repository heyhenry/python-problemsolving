"""28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 
Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""
def str_Str(haystack : str, needle: str) -> int:

    # by default have the needle_index as -1, in the case that no matches are found, 
    # -1 is considered the fail case that denotes this
    needle_index = -1

    for i in range(len(haystack)):
        # check if the given character [i] matches the first character in needle
        if haystack[i] == needle[0]:
            # if it matches, then check if the respective following positions and initially match characters
            # match the characters that make up of needle (in order)
            if haystack[i:i+len(needle)] == needle:
                # if so, mark the first instance aka the first char's index position 
                # that started the validation checking
                needle_index = i
                # once this condition has been met once, break the for loop 
                # as we only want the first matched occurence
                break

    # return the stored position where the char first matched
    return needle_index

def main():
    print(str_Str('sadbutsad', 'sad'))
    print(str_Str('leetcode', 'leeto'))

if __name__ == "__main__":
    main()