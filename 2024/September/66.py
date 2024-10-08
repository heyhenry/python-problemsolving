"""
66. Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""
def plus_one(digits : list[int]) -> list[int]:

    # create a num string variable to store the face value length of the digits list
    num = ''
    # loop through the digits list and append each integer to the num string variable
    for i in digits:
        num += str(i)
    # implement the required logic
    # add the requested one to the num that has been changed to an int type for said calculation
    num = int(num) + 1
    # update the current digits list with the new value/s
    digits[:] = [int(i) for i in str(num)]
    # return the updated digits list
    return digits

def main():
    print(plus_one(digits = [1,2,3]))
    print(plus_one(digits = [4,3,2,1]))
    print(plus_one(digits = [9]))

if __name__ == "__main__":
    main()