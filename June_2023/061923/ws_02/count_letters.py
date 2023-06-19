"""
Returns the count of each letter in `s` as a dictionary
Examples (dictionary print order doesn't matter):
count_letters("") -> {}
count_letters("abc") -> {'a' : 1, 'b' : 1, 'c' : 1}
count_letters("aaaa") -> {'a' : 4}
count_letters("ababbcca) -> {'a' : 3, 'b' : 3, 'c' : 2}
"""

# def count_letters(s : str) -> dict[str, int]:

#     d = {}
#     a_counter = 0
#     b_counter = 0
#     c_counter = 0

#     for i in s:
#         if i == 'a':
#             a_counter += 1
#         if i == 'b':
#             b_counter += 1
#         if i == 'c':
#             c_counter += 1

#     if a_counter > 0:
#         d['a'] = a_counter
#     if b_counter > 0:
#         d['b'] = b_counter
#     if c_counter > 0:
#         d['c'] = c_counter

#     return d

def count_letters(s : str) -> dict[str, int]:

    d = dict()
    d_set = ''.join(set(s))

    for i in d_set:
        d[i] = 0
    
    for i in s:
        if i in d:
            d[i] += 1
    
    return d

def main():

    print(count_letters(""))
    print(count_letters("abc"))
    print(count_letters("aaaa"))
    print(count_letters("ababbcca"))


if __name__ == "__main__":
    main()



# First version - Output not exactly as per examples but does give correct answers
# def count_letters(s : str) -> dict[str, int]:

#     d = {}
#     a_counter = 0
#     b_counter = 0
#     c_counter = 0

#     for i in s:
#         if i == 'a':
#             a_counter += 1
#         if i == 'b':
#             b_counter += 1
#         if i == 'c':
#             c_counter += 1
    
#     if a_counter < 1 and b_counter < 1 and c_counter < 1:
#         return d
#     else:
#         d = dict(a=a_counter, b=b_counter, c=c_counter)

#     return d