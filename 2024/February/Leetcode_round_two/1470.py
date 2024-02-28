def shuffle(nums : list[str], n : int) -> list[int]:

    results = []
    y_list = []

    for i in range(len(nums)//2, len(nums)):
        y_list.append(nums[i])

    for i in range(n):
        results.append(nums[i])
        results.append(y_list[i])

    return results

def main():
    print(shuffle(nums = [2,5,1,3,4,7], n = 3))
    print(shuffle(nums = [1,2,3,4,4,3,2,1], n = 4))
    print(shuffle(nums = [1,1,2,2], n = 2))

if __name__ == "__main__":
    main()