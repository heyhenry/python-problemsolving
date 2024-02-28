def arrayStringAreEqual(word1 : list[str], word2 : list[str]) -> bool:

    return "".join(word1) == "".join(word2)

def main():
    print(arrayStringAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"]))
    print(arrayStringAreEqual(word1 = ["a", "cb"], word2 = ["ab", "c"]))
    print(arrayStringAreEqual(word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]))

if __name__ == "__main__":
    main()