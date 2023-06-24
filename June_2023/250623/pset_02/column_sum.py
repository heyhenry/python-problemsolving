def column_sum(mat : list[list[int]]) -> list[int]:
"""
Returns the sum of each column of the _rectangular_ matrix `mat`
(rectangular means each row is the same length)
Examples:
column_sum([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9] # yes, I did it right this
time
column_sum([[], []]) -> [0]
column_sum([[2, 2], [-1, -2], [3, 9]]) -> [4, 9]
"""