def sumOfUnique(nums : list[int]) -> int:

    result = 0

    u_nums = set(nums)

    for i in u_nums:
        if nums.count(i) == 1:
            result += i

    return result

def main():
    print(sumOfUnique(nums = [1,2,3,2]))
    print(sumOfUnique(nums = [1,1,1,1,1]))
    print(sumOfUnique(nums = [1,2,3,4,5]))

if __name__ == "__main__":
    main()