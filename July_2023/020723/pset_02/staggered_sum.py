"""
Returns the sum of elements in `lst`, which is a list of integers _or_ lists
Examples:
staggered_sum([1, 2, 3]) -> 6
staggered_sum([[], [], []]) -> 0
staggered_sum([[1, 2], 3, [4, 5]]) -> 15
staggered_sum([-4, [-3, 2, 1], 6, 8, [-1]]) -> 9
"""
def staggered_sum(lst : list[int | list[int]]) -> int:

    sum_value = 0

    for i in lst:
        if isinstance(i, list):
            for x in i:
                sum_value += x
        else:
            sum_value += i

    return sum_value

def main():
    print(staggered_sum([1, 2, 3]))
    print(staggered_sum([[], [], []]))
    print(staggered_sum([[1, 2], 3, [4, 5]]))
    print(staggered_sum([-4, [-3, 2, 1], 6, 8, [-1]]))

if __name__ == "__main__":
    main()