"""
1108. Defanging an IP Address

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:

The given address is a valid IPv4 address.
"""
def defang_ip_addr(address : str) -> str:

    n = len(address)
    result = ''

    for i in range(n):
        if address[i] != '.':
            result += address[i]
        else:
            result += '[.]'

    return result

def main():
    print(defang_ip_addr(address = "1.1.1.1"))
    print(defang_ip_addr(address = "255.100.50.0"))

if __name__ == "__main__":
    main()