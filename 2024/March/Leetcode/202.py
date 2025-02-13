"""
202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1
"""
def is_happy(n : int) -> bool:

    called_nums = set()
    calculating = True
    holder = n
    result = True
    
    while calculating:
        temp = 0
        if holder in called_nums:
            result = False
            calculating = False
        else:
            called_nums.add(holder)
            for i in str(holder):
                temp += int(i)**2
            if temp == 1:
                break
            else:
                holder = temp

    return result

def main():
    print(is_happy(n = 19))
    print(is_happy(n = 2))

if __name__ == "__main__":
    main()