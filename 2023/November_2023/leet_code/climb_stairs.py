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
    
    # fibonacci series
        
    result = n

    if n <= 2:
        result = n
    else:
        prev_step_1 = 1
        prev_step_2 = 2
        current = 0
        for _ in range(2, n):
            current = prev_step_1 + prev_step_2
            prev_step_1 = prev_step_2
            prev_step_2 = current

        result = current

    return result

def main():
    print(climb_stairs(2))
    print(climb_stairs(3))
    print(climb_stairs(5)) # should be 8
    print(climb_stairs(44)) # should be 1134903170

if __name__ == "__main__":
    main()

# Update: Had to look at solution + explanation vid. Realised it used the fibonacci series 
# and still took a bit to get the for loop logic to work without just continually referring to solution. 

# Opted to refer to fibonacci series instead of continuosly looking at code solution, took a bit but got there in the end.