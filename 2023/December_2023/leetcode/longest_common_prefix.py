"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
def longest_common_prefix(strs : list[str]) -> str:

    found_prefix = ''
    
    # to find the minimum feasible column length
    stopper = min(strs, key=len)

    for col in range(len(stopper)):
        # to track potential prefix appendages
        prefix_tracker = ''
        for row in range(len(strs)):
            # iterating through first character of each element, rather than per row
            # then adding them to the prefix_tracker for future validation
            prefix_tracker += strs[row][col]
        # checking whether the prefix_tracker contains the same chars throughout its length,
        # which would that, at that point in the iteration all the elements either had the same char in the same position or not
        if prefix_tracker == len(prefix_tracker) * prefix_tracker[0]:
            # if it did, add them to the end result (found_prefix)
            found_prefix += prefix_tracker[0]
        else:
            # break at the first instance the validation does not find a char match across the length of the accrued prefix_tracker
            break

    # second validation process to check the length of the given prefix
    # for a prefix to be viable it needs to have more than 1 matching char across all elements
    # else return an empty string
    if len(found_prefix) < 2:
        found_prefix = ''
    
    return found_prefix

def main():
    print(longest_common_prefix(["flower","flow","flight"]))
    print(longest_common_prefix(["dog","racecar","car"]))
    print(longest_common_prefix(["water", "winter", "winner"]))

if __name__ == "__main__":
    main()