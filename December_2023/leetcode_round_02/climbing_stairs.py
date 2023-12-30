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

    steps_left = n
    
    # just to see what kind of steps were taken
    steps_taken = []

    while steps_left > 0:

        if steps_left - 2 >= 0:
            steps_left -= 2
            steps_taken.append(2)
        else:
            steps_left -= 1
            steps_taken.append(1)
    
    steps_left += n
    print(steps_taken)
    return steps_left   

def main():
    print(climb_stairs(2))
    print(climb_stairs(3))

if __name__ == "__main__":
    main()