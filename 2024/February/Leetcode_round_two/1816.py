def truncateSentences(s : str, k : int) -> str:

    trunced = ''
    s = s.split(' ')
    
    for i in range(0, k):
        if i != k - 1:
            trunced += s[i] + ' '
        else:
            trunced += s[i]

    return trunced

def main():
    print(truncateSentences(s = "Hello how are you Contestant", k = 4))
    print(truncateSentences(s = "What is the solution to this problem", k = 4))
    print(truncateSentences(s = "chopper is not a tanuki", k = 5))

if __name__ == "__main__":
    main()