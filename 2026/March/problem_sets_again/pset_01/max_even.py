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
    results = []
    for i in lst:
        if abs(i) % 2 == 0:
            results.append(i)
    if len(results) == 0:
        return None
    return max(results)

print(max_even([1, 2, 3]))
print(max_even([-4, 3, -1, -6]))
print(max_even([1, 3, 5]))
print(max_even([0]))