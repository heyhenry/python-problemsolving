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

1 <= n <= 45
"""
def climb_stairs(n: int) -> int:

    result = 0

    if n == 1:
        result = n
    elif n == 2:
        result = n
    else:
        step_one = 0
        step_two = 1
        next_step = 0

        for _ in range(n):
            next_step = step_one + step_two
            step_one = step_two
            step_two = next_step
        
        result = next_step
    
    return result

def main():
    print(climb_stairs(2))
    print(climb_stairs(3))
    print(climb_stairs(4))

if __name__ == "__main__":
    main()