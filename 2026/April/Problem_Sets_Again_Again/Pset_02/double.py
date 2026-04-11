""" 
Returns nothing 
Modifies table in place to double each number  
    Examples: 
    double([[1, 2], [3, 4, 5]]) changes lst to [[2, 4], [6, 8, 10]] 
    double([[-1], [-2], [0, 0]]) changes lst to [[-2], [-4], [0, 0]] 
    double([[]]) does "nothing" 
"""
def double(table : list[list[int]]):
    pass

test_case_01 = [[1, 2], [3, 4, 5]]
test_case_02 = [[-1], [-2], [0, 0]]
test_case_03 = [[]]

print("Before Double Function Called:")
print(test_case_01)
print(test_case_02)
print(test_case_03)

# Double function invoked
double(test_case_01)
double(test_case_02)
double(test_case_03)

print("After Double Function Called:")
print(test_case_01)
print(test_case_02)
print(test_case_03)