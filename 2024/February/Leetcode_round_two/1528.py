def restoreString(s : str, indices : list[int]) -> str:

    result = ''
    s_dict = {}
    
    for i in range(len(indices)):
        s_dict[indices[i]] = s[i]

    for key, val in sorted(s_dict.items()):
        result += val
        
    return result

def main():
    print(restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
    print(restoreString(s = "abc", indices = [0,1,2]))

if __name__ == "__main__":
    main()