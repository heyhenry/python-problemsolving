"""
Returns the minimum of the four given integers
Examples:
min_four(1, 2, 3, 4) -> 1
min_four(3, 2, 4, 6) -> 2
min_four(0, 0, -5, 0) -> -5
"""
# solution 1 - Using the min function
# def min_four(x : int, y : int, z : int, w : int) -> int:

#     return min(x, y, z, w)

# solution 2 - Using the max function
# def min_four(x : int, y : int, z : int, w : int) -> int:

#     nums = [x, y, z, w]

#     while len(nums) > 1:

#         mnum = max(nums)
#         nums.remove(mnum)

#     return nums[0]

# solution 3 - Process of elimination 
# def min_four(x : int, y : int, z : int, w : int) -> int:

#     min_num = 0

#     if x < y:
#         if x < z:
#             if x < w:
#                 min_num = x
#             else: 
#                 min_num = w
#         elif z < w:
#             min_num = z
#         else:
#             min_num = w
#     elif y < z:
#         if y < w:
#             min_num = y
#         else:
#             min_num = w
#     elif z < w:
#         min_num = z
#     else:
#         min_num = w

#     return min_num

# solution 4 - Using For Loop
# def min_four(x : int, y : int, z : int, w : int) -> int:

#     nums = [x, y, z, w]
    
#     min_num = None
    
#     for i in nums:
#         if min_num is None or i < min_num:
#             min_num = i
    
#     return min_num

# solution 5 - Using a single variable as point of changing leverage
def min_four(x : int, y : int, z : int, w : int) -> int:

    min_num = x

    if y < min_num:
        min_num = y
    elif z < min_num:
        min_num = z
    elif w < min_num: 
        min_num = w
    
    return min_num

def main():
    print(min_four(1, 2, 3, 4))
    print(min_four(3, 2, 4, 6))
    print(min_four(0, 0, -5, 0))

if __name__ == "__main__":
    main()
