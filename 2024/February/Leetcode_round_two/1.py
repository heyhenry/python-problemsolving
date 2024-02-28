def twoSum(nums : list[int], target : int) -> list[int]:

    result = None

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                result = [i,j]
                break

    return result

def main():
    print(twoSum(nums = [2,7,11,15], target = 9))
    print(twoSum(nums = [3,2,4], target = 6))
    print(twoSum(nums = [3,3], target = 6))

if __name__ == "__main__":
    main()