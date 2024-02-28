def longestCommonPrefix(strs : list[str]) -> str:

    prefix = ''

    iterations = len(min(strs, key=len))
    
    for col in range(iterations):
        stack = []
        for row in range(len(strs)):
            stack.append(strs[row][col])
        if len(set(stack)) == 1:
            prefix += stack[0]
        else:
            break 

    return prefix

def main():
    print(longestCommonPrefix(strs = ["flower","flow","flight"]))
    print(longestCommonPrefix(strs = ["dog","racecar","car"]))

if __name__ == "__main__":
    main()