def findNumbers(nums : list[int]) -> int:

    even_count = 0

    for i in nums:
        if len(str(i)) % 2 == 0:
            even_count += 1 

    return even_count

def main():
    print(findNumbers(nums = [12,345,2,6,7896]))
    print(findNumbers(nums = [555,901,482,1771]))

if __name__ == "__main__":
    main()