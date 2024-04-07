"""
263. Ugly Number

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

 

Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
Example 3:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.
 

Constraints:

-231 <= n <= 231 - 1
"""
def dest_city(paths : list[list[str]]) -> str:

    travelling = [i[0] for i in paths]

    for i in paths:
        if i[1] not in travelling:
            return i[1]

def main():
    print(dest_city(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
    print(dest_city(paths = [["B","C"],["D","B"],["C","A"]]))
    print(dest_city(paths = [["A","Z"]]))

if __name__ == "__main__":
    main()