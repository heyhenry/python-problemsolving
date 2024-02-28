def threeConsecutive(arr : list[int]) -> bool:

    result = False
    counter = 0
    for i in arr:
        if i % 2 != 0:
            counter += 1
        else:
            counter = 0
        if counter == 3:
            result = True
            break

    return result

def main():
    print(threeConsecutive(arr = [2,6,4,1]))
    print(threeConsecutive(arr = [1,2,34,3,4,5,7,23,12]))

if __name__ == "__main__":
    main()