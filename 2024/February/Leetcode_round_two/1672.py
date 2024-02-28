def maximumWealth(accounts : list[int]) -> int:

    bals = []

    for i in accounts:
        bals.append(sum(i))

    return max(bals)

def main():
    print(maximumWealth(accounts = [[1,2,3],[3,2,1]]))
    print(maximumWealth(accounts = [[1,5],[7,3],[3,5]]))
    print(maximumWealth(accounts = [[2,8,7],[7,1,3],[1,9,5]]))

if __name__ == "__main__":
    main()