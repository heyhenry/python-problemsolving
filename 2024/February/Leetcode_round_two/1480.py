def runningSum(nums : list[int]) -> list[int]:

    results = []
    num = 0

    for i in nums:
        num += i
        results.append(num)    
    
    return results

def main():
    print(runningSum(nums = [1,2,3,4]))
    print(runningSum(nums = [1,1,1,1,1]))
    print(runningSum(nums = [3,1,2,10,1]))

if __name__ == "__main__":
    main()