"""
Returns the maximum even number in `lst`, or `None` if none exists
Note that negatives are even if the associated positive is
Examples:
max_even([1, 2, 3]) -> 2
max_even([-4, 3, -1, -6]) -> -4
max_even([1, 3, 5]) -> None
max_even([0]) -> 0
"""
class Problem:
    def max_even(self, lst : list[int]) -> int | None:
        even_nums = []
        for i in lst:
            if abs(i) % 2 == 0:
                even_nums.append(i)
        if even_nums:
            return max(even_nums)
        return None

test_01 = [1, 2, 3]
test_02 = [-4, 3, -1, -6]
test_03 = [1, 3, 5]
test_04 = [0]

p = Problem()

print(p.max_even(test_01))
print(p.max_even(test_02))
print(p.max_even(test_03))
print(p.max_even(test_04))