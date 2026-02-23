"""
Returns the sum of each row of the table as a list
Examples:
sum_all([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
sum_all([[2], [4, 7], [-1, -2, -4, -5]]) -> [2, 11, -12]
sum_all([[]]) -> []
"""
class Problem:
    def sum_all(self, table : list[list[int]]) -> list[int]:
        results = []
        for row in table:
            results.append(sum(row))
        return results

test_01 = [[1, 2, 3], [4, 5, 6]]
test_02 = [[2], [4, 7], [-1, -2, -4, -5]]
test_03 = [[]]

p = Problem()

print(p.sum_all(test_01))
print(p.sum_all(test_02))
print(p.sum_all(test_03))