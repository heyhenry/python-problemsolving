"""
746. Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 

Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""
def min_cost_climbing_stairs(cost: list[int]) -> int:

    cost_accumulation = 0
    steps_left = len(cost)

    if len(cost) == 1:
        cost_accumulation += cost[0]
        steps_left -= 1
    elif len(cost) == 2:
        if cost[1] < cost[0]:
            cost_accumulation += cost[1]
            steps_left -= 1
        else:
            cost_accumulation += cost[0] + cost[1]
            steps_left -= 1
    elif len(cost) == 3:
        if cost[1] < cost[0] + cost[1]:
            cost_accumulation += cost[1]
            steps_left -= 2
        else:
            cost_accumulation += [0]
            steps_left -= 1
    else:
        two_steps_taken = False

        if cost[1] <= cost[0]:
            
            for i in range(1, len(cost)):
                if two_steps_taken:
                    two_steps_taken = False
                    continue

                if i+1 <= len(cost) - 1 and cost[i] > cost[i+1]:
                    two_steps_taken = True
                    cost_accumulation += cost[i+1]
                    steps_left -= 2
                else:
                    cost_accumulation += cost[i]
                    steps_left -= 1
        else:
            two_steps_taken = False

            for i in range(len(cost)):
                if two_steps_taken:
                    two_steps_taken = False
                    continue

                if cost[i] >= cost[i+1]:
                    two_steps_taken = True
                    cost_accumulation += cost[i+1]
                    steps_left -= 2
                else:
                    cost_accumulation += cost[i]
                    steps_left -= 1            

    return cost_accumulation 

def main():
    print(min_cost_climbing_stairs([10,15,20]))
    print(min_cost_climbing_stairs([1,100,1,1,1,100,1,1,100,1]))

if __name__ == "__main__":
    main()