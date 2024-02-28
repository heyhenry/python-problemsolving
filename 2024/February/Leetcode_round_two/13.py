def romanToInt(s : str) -> int:

    result = 0
    skip_iteration = False
    romans = {
        'I' : 1, 
        'L' : 50,
        'V' : 5, 
        'M' : 1000, 
        'CM': 900,
        'XC' : 90,
        'IV' : 4, 
        'X': 10, 
        'C': 100,
        'IX' : 9, 
        'D': 500, 
        'CD': 400, 
        'XL' : 40
    }
    
    for i in range(len(s)):
        if skip_iteration:
            skip_iteration = False
            continue
        if i != len(s) - 1 and s[i] + s[i+1] in romans:
            result += romans[s[i]+s[i+1]]
            skip_iteration = True
        if skip_iteration == False:
            result += romans[s[i]]

    return result

def main():
    print(romanToInt(s = "III"))
    print(romanToInt(s = "LVIII"))
    print(romanToInt(s = "MCMXCIV"))

if __name__ == "__main__":
    main()