def threeSum(nums : list[int]) -> list[list[int]]:

    # results = []
    # sorted_filter = []

    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         for k in range(j+1, len(nums)):
    #             if (i != j and i != k and j != k) and (nums[i]+nums[j]+nums[k] == 0) and [nums[i],nums[j],nums[k]] not in results:
    #                 if sorted([nums[i],nums[j],nums[k]]) not in sorted_filter:
    #                     sorted_filter.append(sorted([nums[i],nums[j],nums[k]]))
    #                     results.append([nums[i],nums[j],nums[k]])   
                
    # return results

    nums.sort()
    results = []
    sorted_filter = []

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if (i != j and i != k and j != k) and (nums[i]+nums[j]+nums[k] == 0) and [nums[i],nums[j],nums[k]] not in results:
                        results.append([nums[i],nums[j],nums[k]])   
                
    return results


def main():
    print(threeSum(nums = [-1,0,1,2,-1,-4]))
    print(threeSum(nums = [0,1,1]))
    print(threeSum(nums = [0,0,0]))

if __name__ == "__main__":
    main()