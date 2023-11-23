import sys 

def roman_to_int(s : str) -> int:
    
    result = 0
    counter = 0

    for c in range(len(s)):
        if counter == len(s):
            break
        if s[c] == 'L': 
            result += 50
            counter += 1
        elif s[c] == 'V':
            result += 5
            counter += 1
        elif s[c] == 'I':
            if c != len(s) - 1:
                if s[c+1] == 'V':
                    result += 4
                    counter += 2
                else:
                    result += 1
                    counter += 1
            else:
                result += 1
                counter += 1
        elif s[c] == 'M':
            if c == 0:
                result += 1000
                counter += 1
            elif s[c-1] == 'C':
                result += 900
                counter += 2
        elif s[c] == 'X':
            if c != len(s) - 1:
                if s[c+1] == 'C':
                    result += 90
                    counter += 2

    return result
            
def main():
    result = sys.argv[1]

    print(roman_to_int(result))

if __name__ == "__main__":
    main()

# some notes to self about solving the problem - Please READ

# The problem solution strictly caters to the provided roman numerals that are being tested on.
# It uses a counter system to realise when all the characters in the string has been accounted for.
# Currently the string has been altered to be a list due to the notion of utilising list's built in functions (remove, replace and pop), 
# however it hasnt gone well as it affected the static iteration course of the s itself as elements were beinga actively removed. 
# Further more it just seemed to cause more confusion and code chaos, encroaching upon code readability.

# I will test the alternative usage of a new list rather than a counter, but I think the counter is still cleaner and requires less code at the end.
# Also remember to transfer the final code solution to the actual problem file instead of residing in the test file.
# Might also remove the list system generally, if maintaining the counter system as it seems to be unnessary, but will trial after break. 