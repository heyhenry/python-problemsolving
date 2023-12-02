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
# solution 1
# def defang_ip(address: str) -> str:

#     defanged_address = ''

#     for c in range(len(address)):
#         if address[c] == '.':
#             defanged_address += '['
#             defanged_address += '.'
#             defanged_address += ']'
#         else:
#             defanged_address += address[c]

#     return defanged_address

# solution 2
def defang_ip(address: str) -> str:

    defanged_addr = ''

    for c in range(len(address)):
        if address[c] == ".":
            defanged_addr += '[.]'
        else:
            defanged_addr += address[c]

    return defanged_addr
    

def main():
    print(defang_ip("1.1.1.1"))
    print(defang_ip("255.100.50.0"))

if __name__ == "__main__":
    main()