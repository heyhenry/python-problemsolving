"""
28. Find the Index of the First Occurrence in a String

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
def str_str(haystack : str, needle : str) -> int:

    n = len(haystack)
    t = len(needle)

    for i in range(n):
        if haystack[i:i+t] == needle:
            
            return i
        
    return -1

def main():
    print(str_str(haystack = "sadbutsad", needle = "sad"))
    print(str_str(haystack = "leetcode", needle = "leeto"))

if __name__ == "__main__":
    main()