""" 
  Returns the maximum even number in `lst`, or `None` if none exists 
  Note that negatives are even if the associated positive is 
  Examples: 
    max_even([1, 2, 3]) -> 2 
    max_even([-4, 3, -1, -6]) -> -4 
    max_even([1, 3, 5]) -> None 
    max_even([0]) -> 0 
"""
def max_even(lst : list[int]) -> int | None:
    def is_even(n : int) -> bool:
        if n % 2 == 0:
            return True
        return False
    
    result = None
    for i in lst:
        if is_even(i) and result is None:
            result = i
        elif is_even(i) and i > result:
            result = i
    return result

print(max_even([1, 2, 3]))
print(max_even([-4, 3, -1, -6]))
print(max_even([1, 3, 5]))
print(max_even([0]))