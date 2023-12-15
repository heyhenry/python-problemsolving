"""
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""
# calculate the int value of a binary string
def calculate_binary(s : str) -> int:

    result = 0

    # loop through formula for each char in binary str respectively
    for i in range(len(s)):
        result += int(s[i]) * (2**(len(s)-i-1))

    return result

# convert int value into binary string
def convert_to_binary(n : int) -> str:

    im_done = True
    result = ''

    # continuously update and iterate through the given number until its value is less than 1 
    # meaning there are no more possible remainders
    while im_done:

        remainder = int(n) % 2
        
        # store the remainders as they will be the binary strings
        result += str(remainder)

        n = int(n) / 2

        if n < 1:
            im_done = False

    final_result = ''

    # the given result is the correct binary strings but in reversed order
    # so loop through it backwards and store into a final_result variable
    for i in range(len(result)-1, -1, -1):
        final_result += result[i]
    
    return final_result

def add_binary(a : str, b : str) -> str:

    sum = calculate_binary(a) + calculate_binary(b)

    return convert_to_binary(sum)

def main():
    print(add_binary("11", "1")) # 100
    print(add_binary("1010", "1011")) # 10101

if __name__ == "__main__":
    main()