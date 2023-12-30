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
def add_binary(a : str, b : str):

    result = ''
    num = '0'
    if len(a) == len(b):

        altered_a = ''
        altered_b = ''
        
        for i in range(len(a)-1, -1, -1):
            altered_a += a[i]
            altered_b += b[i]

        for i in range(len(a)):
            if (int(altered_a[i]) + int(altered_b[i]) + int(num)) > 1:
                if i == (len(a)-1):
                    result += '01'
                    num = '1'
                else:
                    result += '0'
                    num = '1'
            else:
                result += '1'
                num = '0'
    else:

        max_positions = len(max(a,b))

        if len(a) < max_positions:
            while len(a) < max_positions:
                a += '0'
            a = a[::-1]

        if len(b) < max_positions:
            while len(b) < max_positions:
                b += '0'
            b = b[::-1]

        while len(a) < max_positions:
            a += '0'

        while len(b) < max_positions:
            b += '0'

        altered_a = ''
        altered_b = ''
        
        for i in range(len(a)-1, -1, -1):
            altered_a += a[i]
            altered_b += b[i]

        altered_result = ''
        for i in range(len(a)):
            if (int(altered_a[i]) + int(altered_b[i]) + int(num)) > 1:
                if i == (len(a)-1):
                    altered_result += '01'
                    num = '1'
                else:
                    altered_result += '0'
                    num = '1'
            else:
                altered_result += '1'
                num = '0'

        for i in range(len(altered_result)-1, -1, -1):
            result += altered_result[i]
        

    return result

def main():
    print(add_binary('1', '11')) # 100
    print(add_binary('1010','1011')) #10101
    print(add_binary('1100', '0011')) 
    print(add_binary('1011', '0110'))

if __name__ == "__main__":
    main()