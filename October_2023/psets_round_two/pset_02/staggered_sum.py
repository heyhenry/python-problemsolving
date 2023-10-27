"""
Returns the sum of elements in `lst`, which is a list of integers _or_ lists
Examples:
staggered_sum([1, 2, 3]) -> 6
staggered_sum([[], [], []]) -> 0
staggered_sum([[1, 2], 3, [4, 5]]) -> 15
staggered_sum([-4, [-3, 2, 1], 6, 8, [-1]]) -> 9
"""
def staggered_sum(lst : list[int | list[int]]) -> int:

    result = 0

    for x in lst:
        if isinstance(x, list):
            for i in x:
                result += i
        else:
            result += x

    return result

def main():
    print(staggered_sum([1, 2, 3]))
    print(staggered_sum([[], [], []]))
    print(staggered_sum([[1, 2], 3, [4, 5]]))
    print(staggered_sum([-4, [-3, 2, 1], 6, 8, [-1]]))

if __name__ == "__main__":
    main()