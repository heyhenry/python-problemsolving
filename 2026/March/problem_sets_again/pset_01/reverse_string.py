""" 
  Returns the string `s` in reverse order 
  Examples: 
    reverse_string('abc') -> 'cba' 
    reverse_string('') -> '' 
    reverse_string('abab') -> 'baba' 
"""
def reverse_string(s : str) -> str:
    rev_s = ""
    for c in s:
        rev_s = c + rev_s
    return rev_s

print(reverse_string('abc'))
print(reverse_string(''))
print(reverse_string('abab'))