"""
Returns the minimum of the four given integers
Examples:
min_four(1, 2, 3, 4) -> 1
min_four(3, 2, 4, 6) -> 2
min_four(0, 0, -5, 0) -> -5
"""
class Problem:
    def min_four(self, x : int, y : int, z : int, w : int) -> int:
        return min(x, y, z, w)

test_01 = [1, 2, 3, 4]
test_02 = [3, 2, 4, 6]
test_03 = [0, 0, -5, 0]

p = Problem()

print(p.min_four(test_01[0], test_01[1], test_01[2], test_01[3]))
print(p.min_four(test_02[0], test_02[1], test_02[2], test_02[3]))
print(p.min_four(test_03[0], test_03[1], test_03[2], test_03[3]))