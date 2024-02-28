def heightChecker(heights : list[int]) -> int:

    mismatch_count = 0

    for i in range(len(sorted(heights))):
        if heights[i] != sorted(heights)[i]:
            mismatch_count += 1

    return mismatch_count

def main():
    print(heightChecker(heights = [1,1,4,2,1,3]))
    print(heightChecker(heights = [5,1,2,3,4]))
    print(heightChecker(heights = [1,2,3,4,5]))

if __name__ == "__main__":
    main()