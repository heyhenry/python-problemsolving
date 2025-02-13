"""
1550. Three Consecutive Odds

Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
"""
def three_consecutive_odds(arr : list[int]) -> bool:

    count = 0
    result = False
    
    for i in arr:
        if i % 2 != 0:
            count += 1
            if count == 3:
                result = True
                break
        else:
            count = 0

    return result
    
def main():
    print(three_consecutive_odds(arr = [2,6,4,1]))
    print(three_consecutive_odds(arr = [1,2,34,3,4,5,7,23,12]))

if __name__ == "__main__":
    main()