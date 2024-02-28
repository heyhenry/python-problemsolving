def sumOddLengthSubarrays(arr : list[int]) -> int:

    sub_arr = []
    result = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            sub_arr.append(arr[i:j])

    for i in sub_arr:
        if len(i) % 2 != 0:
            result += sum(i)

    return result

def main():
    print(sumOddLengthSubarrays(arr = [1,4,2,5,3]))
    print(sumOddLengthSubarrays(arr = [1,2]))
    print(sumOddLengthSubarrays(arr = [10,11,12]))

if __name__ == "__main__":
    main()