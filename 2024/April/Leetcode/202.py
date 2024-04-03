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

    storage = []

    while n >= 1:

        new_n = 0

        for i in str(n):
            new_n += int(i)**2
        
        
        if new_n not in storage: 
            storage.append(new_n)
            n = new_n
        else:
            break

        if n == 1:
            return True
        
    return False
    
def main():
    print(is_happy(n = 19))
    print(is_happy(n = 2))

if __name__ == "__main__":
    main()