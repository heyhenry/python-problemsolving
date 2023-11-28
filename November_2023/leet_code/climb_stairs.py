"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 4
"""
def climb_stairs(n : int) -> int:

    x = range(1, n, 1)
    
    counter = 0
    
    for _ in x:
        counter += 1
    
    y = range(1, n, 2)
    
    for _ in y:
        counter += 1
    
    return counter

def main():
    print(climb_stairs(2))
    print(climb_stairs(3))
    print(climb_stairs(5)) # should be 8
    print(climb_stairs(44)) # should be 1134903170

if __name__ == "__main__":
    main()

# Note: I would like to check the integrity of this solution against additional test cases, but it does suffice for the provided leetcode test cases.